"""
Kalaignar Digital Library
Extractor Engine v1

Part 1 - Foundation

Responsibilities
----------------
✓ Load configuration
✓ Read book metadata
✓ Read volume definitions
✓ Locate raw HTML folders
✓ Create extracted folders
✓ Utility functions
✓ Metadata helpers

HTML parsing begins in Part 2.
"""

from pathlib import Path
import json
import yaml
from bs4 import BeautifulSoup
import re


class Extractor:

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

    ####################################################################
    # Summary
    ####################################################################

    def print_summary(self):

        print()
        print("=" * 70)
        print(self.project["name"])
        print("=" * 70)

        print(f"Book     : {self.book['title']}")
        print(f"Author   : {self.book['author']}")
        print(f"Volumes  : {len(self.volumes)}")

        print("=" * 70)

    ####################################################################
    # Volume Lookup
    ####################################################################

    def get_volume(self, volume_id):

        for volume in self.volumes:

            if volume["id"] == volume_id:
                return volume

        raise ValueError(
            f"Volume {volume_id} not found."
        )

    ####################################################################
    # Folder Helpers
    ####################################################################

    def raw_folder(self, volume):

        return Path(volume["output"])

    ####################################################################

    def extracted_folder(self, volume):

        folder = Path(
            str(volume["output"]).replace(
                "/raw/",
                "/extracted/"
            )
        )

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        return folder

    ####################################################################
    # File Helpers
    ####################################################################

    def html_files(self, volume):

        folder = self.raw_folder(volume)

        return sorted(folder.glob("*.html"))

    ####################################################################

    def output_file(self, volume, html_file):

        folder = self.extracted_folder(volume)

        return folder / f"{html_file.stem}.md"

    ####################################################################

    def metadata_file(self, volume):

        folder = self.extracted_folder(volume)

        return folder / "metadata.json"

    ####################################################################

    def already_extracted(self, volume, html_file):

        return self.output_file(
            volume,
            html_file
        ).exists()

    ####################################################################
    # Metadata
    ####################################################################

    def save_metadata(self, volume, metadata):

        with open(

            self.metadata_file(volume),

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
    # HTML Loader
    ####################################################################

    def load_html(self, html_file):

        return html_file.read_text(

            encoding="utf-8",

            errors="ignore"

        )

    ####################################################################
    # Parse HTML
    ####################################################################

    def parse_html(self, html):

        return BeautifulSoup(

            html,

            "lxml"

        )

    ####################################################################
    # Locate Book Text
    ####################################################################

    def get_page_container(self, soup):

        #
        # Tamil Wikisource stores OCR text inside div.pagetext
        #

        page = soup.select_one("div.pagetext")

        if page:

            return page

        #
        # Fallbacks
        #

        selectors = [

            ".prp-page-content",

            "#mw-content-text",

            ".mw-parser-output"

        ]

        for selector in selectors:

            node = soup.select_one(selector)

            if node:

                return node

        return None

    ####################################################################
    # Remove Wikisource UI
    ####################################################################

    def remove_noise(self, page):

        selectors = [

            ".prp-page-qualityheader",

            ".wst-running-header",

            ".mw-editsection",

            ".wst-dhr",

            ".mw-cite-backlink",

            ".reference",

            "script",

            "style",

            "noscript"

        ]

        for selector in selectors:

            for tag in page.select(selector):

                tag.decompose()

    ####################################################################
    # Clean Extracted Text
    ####################################################################

    def clean_text(self, text):

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:

                continue

            #
            # Remove Wikisource footer
            #

            if "இலிருந்து மீள்விக்கப்பட்டது" in line:
                continue

            if "மெய்ப்பு பார்க்கப்பட்டுள்ளது" in line:
                continue

            if line.startswith("↑"):
                continue

            #
            # Collapse whitespace
            #

            line = re.sub(

                r"\s+",

                " ",

                line

            )

            lines.append(line)

        return "\n".join(lines)

    ####################################################################
    # Extract One Page
    ####################################################################

    def extract_page(self, html):

        soup = self.parse_html(html)

        page = self.get_page_container(soup)

        if page is None:

            return ""

        self.remove_noise(page)

        text = page.get_text("\n")

        return self.clean_text(text)

    ####################################################################
    # Markdown Writer
    ####################################################################

    def write_markdown(

        self,

        volume,

        html_file,

        text

    ):

        page = int(html_file.stem)

        output = self.output_file(

            volume,

            html_file

        )

        source = volume["url_template"].format(

            page=page

        )

        markdown = f"""---
book: {self.book['title']}
volume: {volume['id']}
page: {page}
source: {source}
---

{text}
"""

        output.write_text(

            markdown,

            encoding="utf-8"

        )
        ####################################################################
    # Process One Page
    ####################################################################

    def process_page(self, volume, html_file):

        #
        # Resume support
        #

        if self.already_extracted(volume, html_file):

            return "skipped"

        html = self.load_html(html_file)

        text = self.extract_page(html)

        if not text.strip():

            return "empty"

        self.write_markdown(

            volume,

            html_file,

            text

        )

        return "done"
        ####################################################################
    # Process One Volume
    ####################################################################

    def process_volume(self, volume):

        print()

        print("=" * 70)

        print(volume["title"])

        print("=" * 70)

        html_files = self.html_files(volume)

        total = len(html_files)

        print(f"Pages found : {total}")

        extracted = 0
        skipped = 0
        empty = 0

        for index, html_file in enumerate(html_files, start=1):

            result = self.process_page(

                volume,

                html_file

            )

            if result == "done":
                extracted += 1

            elif result == "skipped":
                skipped += 1

            else:
                empty += 1

            #
            # Progress
            #

            if index % 25 == 0 or index == total:

                print(

                    f"{index}/{total} pages processed"

                )

        metadata = {

            "book": self.book["title"],

            "volume": volume["id"],

            "title": volume["title"],

            "pages": total,

            "extracted": extracted,

            "skipped": skipped,

            "empty": empty

        }

        self.save_metadata(

            volume,

            metadata

        )

        print()

        print("Finished")

        print(metadata)
    ####################################################################
    # Run Extractor
    ####################################################################

    def run(self):

        self.print_summary()

        print()

        for volume in self.volumes:
exit
            self.process_volume(volume)

        print()

        print("=" * 70)

        print("Extraction Complete")

        print("=" * 70)
    
###############################################################
# Entry Point
###############################################################

def main():

    extractor = Extractor()

    extractor.run()


if __name__ == "__main__":

    main()
