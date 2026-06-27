#!/usr/bin/env python3
"""
Kalaignar Digital Library
download.py

Downloads every Wikisource page for each volume defined
in config.yaml.

Features
--------
✓ Resume support
✓ Skip existing pages
✓ Automatic end detection
✓ Retry failed downloads
✓ Logging
✓ Multi-volume support

Author:
Kalaignar Digital Library Project
"""

import os
import time
import logging
from pathlib import Path

import yaml
import requests
from bs4 import BeautifulSoup

CONFIG_FILE = "config.yaml"


# --------------------------------------------------
# Logging
# --------------------------------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/download.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger("").addHandler(console)


# --------------------------------------------------
# Load Config
# --------------------------------------------------

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

network = config["network"]

TIMEOUT = network.get("timeout", 20)
DELAY = network.get("delay_seconds", 1)
RETRIES = network.get("retries", 3)
MAX_MISSING = network.get("max_missing_pages", 25)


HEADERS = {
    "User-Agent":
        "Kalaignar-Digital-Library/2.0 "
        "(Educational Archival Project)"
}


# --------------------------------------------------
# Helpers
# --------------------------------------------------

def download_page(url):
    """
    Download a single HTML page.
    """

    for attempt in range(RETRIES):

        try:

            r = requests.get(
                url,
                timeout=TIMEOUT,
                headers=HEADERS
            )

            if r.status_code == 200:
                return r.text

            if r.status_code == 404:
                return None

        except requests.RequestException:

            logging.warning(
                f"Retry {attempt+1} : {url}"
            )

            time.sleep(2)

    return None


def has_wikisource_content(html):

    soup = BeautifulSoup(html, "html.parser")

    content = soup.find("div", class_="mw-parser-output")

    if content is None:
        return False

    text = content.get_text(strip=True)

    return len(text) > 100


# --------------------------------------------------
# Download Volume
# --------------------------------------------------

def process_volume(volume):

    output = Path(volume["output"])
    output.mkdir(parents=True, exist_ok=True)

    base = volume["url"]

    logging.info("")
    logging.info("=" * 60)
    logging.info(f"Downloading {volume['title']}")
    logging.info("=" * 60)

    page = 1
    missing = 0

    while True:

        filename = output / f"{page:04d}.html"

        if filename.exists():

            logging.info(
                f"Page {page:04d}  ✓ Exists"
            )

            page += 1
            missing = 0
            continue

        url = f"{base}/{page}"

        logging.info(
            f"Downloading page {page}"
        )

        html = download_page(url)

        if html is None:

            missing += 1

            logging.info(
                f"Missing page {page} "
                f"({missing}/{MAX_MISSING})"
            )

            if missing >= MAX_MISSING:

                logging.info("")
                logging.info(
                    f"Finished {volume['title']}"
                )

                break

            page += 1
            continue

        if not has_wikisource_content(html):

            missing += 1

            logging.info(
                f"No content page {page}"
            )

            if missing >= MAX_MISSING:
                break

            page += 1
            continue

        missing = 0

        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

        logging.info(
            f"Saved {filename.name}"
        )

        time.sleep(DELAY)

        page += 1


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():

    logging.info("")
    logging.info("=" * 70)
    logging.info("Kalaignar Digital Library")
    logging.info("Downloader Started")
    logging.info("=" * 70)

    for volume in config["volumes"]:

        process_volume(volume)

    logging.info("")
    logging.info("=" * 70)
    logging.info("Download Complete")
    logging.info("=" * 70)


if __name__ == "__main__":
    main()