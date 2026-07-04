"""
Kalaignar Digital Library
Downloader Engine v4

Part 1
-------

Responsibilities

✓ Load config.yaml
✓ Read project metadata
✓ Read volume definitions
✓ Create HTTP session
✓ Prepare retry strategy
✓ Utility functions

Downloading logic will be added in Part 2.
"""

from pathlib import Path
import json
import time

import yaml
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class Downloader:

    ####################################################################
    # Initialization
    ####################################################################

    def __init__(self, config_file="config.yaml"):

        self.root = Path.cwd()

        self.config_path = self.root / config_file

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Config file not found:\n{self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

        self.project = self.config["project"]
        self.book = self.config["book"]
        self.volumes = self.config["volumes"]

        network = self.config.get("network", {})

        self.timeout = network.get("timeout", 20)
        self.delay = network.get("delay_seconds", 1)
        self.retries = network.get("retries", 3)
        self.max_missing = network.get("max_missing_pages", 30)

        self.session = self.create_session()

    ####################################################################
    # HTTP Session
    ####################################################################

    def create_session(self):

        session = requests.Session()

        retry = Retry(

            total=self.retries,

            connect=self.retries,

            read=self.retries,

            backoff_factor=1.5,

            status_forcelist=[

                429,
                500,
                502,
                503,
                504

            ],

            allowed_methods=["GET"]

        )

        adapter = HTTPAdapter(max_retries=retry)

        session.mount("https://", adapter)
        session.mount("http://", adapter)

        session.headers.update({

            "User-Agent":
                "KalaignarDigitalLibrary/4.0"

        })

        return session

    ####################################################################
    # Utility Functions
    ####################################################################

    def get_volume(self, volume_id):

        for volume in self.volumes:

            if volume["id"] == volume_id:
                return volume

        raise ValueError(
            f"Volume {volume_id} not found."
        )

    ####################################################################

    def prepare_folder(self, volume):

        folder = Path(volume["output"])

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    ####################################################################

    def html_file(self, folder, page):

        return folder / f"{page:04}.html"

    ####################################################################

    def metadata_file(self, folder):

        return folder / "metadata.json"

    ####################################################################

    def page_exists(self, folder, page):

        return self.html_file(folder, page).exists()

    ####################################################################

    def save_metadata(self, folder, metadata):

        with open(

            self.metadata_file(folder),

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                metadata,

                f,

                ensure_ascii=False,

                indent=2

            )

    ####################################################################
    # Display Summary
    ####################################################################

    def print_summary(self):

        print("=" * 60)

        print(self.project["name"])

        print("=" * 60)

        print(f"Book     : {self.book['title']}")
        print(f"Author   : {self.book['author']}")
        print(f"Volumes  : {len(self.volumes)}")
        print(f"Timeout  : {self.timeout}")
        print(f"Retries  : {self.retries}")
        print(f"Delay    : {self.delay}")

        print("=" * 60)
        ####################################################################
    # URL Builder
    ####################################################################

    def build_url(self, volume, page):
        """
        Build the Wikisource URL for a page using the template
        defined in config.yaml.
        """

        return volume["url_template"].format(page=page)

    ####################################################################
    # HTML Validation
    ####################################################################

    def is_valid_page(self, html):
        """
        Returns True only if the downloaded HTML contains
        an actual Wikisource page.
        """

        invalid_strings = [

            "There is currently no text",
            "Wikisource does not yet have a page",
            "No such special page",
            "404 Not Found",
            "The page does not exist"

        ]

        for text in invalid_strings:
            if text.lower() in html.lower():
                return False

        return True

    ####################################################################
    # Download One Page
    ####################################################################

    def download_page(self, volume, folder, page):

        filename = self.html_file(folder, page)

        # Resume support
        if filename.exists():

            print(f"✓ Page {page} already downloaded")

            return "exists"

        url = self.build_url(volume, page)

        print(f"Downloading page {page}")

        try:

            response = self.session.get(

                url,

                timeout=self.timeout

            )

        except Exception as e:

            print(e)

            return "missing"

        if response.status_code != 200:

            return "missing"

        html = response.text

        if not self.is_valid_page(html):

            return "missing"

        filename.write_text(

            html,

            encoding="utf-8"

        )

        time.sleep(self.delay)

        return "downloaded"
        ####################################################################
    # Resume Support
    ####################################################################

    def get_resume_page(self, folder):
        """
        Returns the next page to download.
        """

        html_files = sorted(folder.glob("*.html"))

        if not html_files:
            return 1

        try:
            last_page = int(html_files[-1].stem)
            return last_page + 1
        except Exception:
            return 1

    ####################################################################
    # Update Metadata
    ####################################################################

    def update_metadata(
        self,
        folder,
        volume,
        last_page,
        downloaded_pages,
        status="completed"
    ):

        metadata = {

            "book": self.book["title"],

            "volume": volume["id"],

            "title": volume["title"],

            "last_page": last_page,

            "downloaded_pages": downloaded_pages,

            "status": status,

            "url_template": volume["url_template"]

        }

        self.save_metadata(
            folder,
            metadata
        )
    
    ####################################################################
    # Download Volume
    ####################################################################

    def download_volume(self, volume_id):

        volume = self.get_volume(volume_id)

        folder = self.prepare_folder(volume)

        print()
        print("=" * 60)
        print(volume["title"])
        print("=" * 60)

        page = self.get_resume_page(folder)

        print(f"Resuming from page {page}")

        downloaded = 0

        missing = 0

        while True:

            result = self.download_page(
                volume,
                folder,
                page
            )

            if result == "downloaded":

                downloaded += 1

                missing = 0

            elif result == "exists":

                missing = 0

            else:

                missing += 1

                print(
                    f"Missing page {page} "
                    f"({missing}/{self.max_missing})"
                )

            if missing >= self.max_missing:

                print()
                print("End of volume detected.")
                break

            page += 1

        self.update_metadata(

            folder,

            volume,

            page - missing,

            downloaded

        )

        print()
        print("-" * 60)
        print("Download Complete")
        print(f"Downloaded : {downloaded}")
        print(f"Last Page  : {page-missing}")
        print("-" * 60)
    
    ####################################################################
    # Download All Volumes
    ####################################################################

    def download_all(self):

        self.print_summary()

        for volume in self.volumes:

            self.download_volume(
                volume["id"]
            )

        print()
        print("=" * 60)
        print("ALL DOWNLOADS FINISHED")
        print("=" * 60)