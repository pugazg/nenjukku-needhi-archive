import os
import time
import requests
import yaml

from pathlib import Path

HEADERS = {
    "User-Agent": "Kalaignar Digital Library Bot/1.0"
}

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config.yaml"

def load_config():
    with open(CONFIG, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_page(url):
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    return response.text


def main():

    config = load_config()

    base = config["source"]["base_url"]

    output = Path(config["storage"]["raw_html"]) / f"volume{config['book']['volume']}"

    output.mkdir(parents=True, exist_ok=True)

    page = 1

    while True:

        url = f"{base}/{page}"

        print(f"Downloading page {page}")

        try:
            html = download_page(url)

        except Exception:

            print("Reached end of volume.")

            break

        filename = output / f"{page:04}.html"

        filename.write_text(html, encoding="utf-8")

        page += 1

        time.sleep(config["network"]["delay_seconds"])


if __name__ == "__main__":
    main()
