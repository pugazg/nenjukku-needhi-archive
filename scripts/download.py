import os
import time
import yaml
import requests
from pathlib import Path

# -----------------------------------------------------
# Load Config
# -----------------------------------------------------

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

storage_root = config["storage"]["root"]

timeout = config["network"]["timeout"]
delay = config["network"]["delay_seconds"]
retries = config["network"]["retries"]
user_agent = config["network"]["user_agent"]

headers = {
    "User-Agent": user_agent
}

# -----------------------------------------------------
# Download Function
# -----------------------------------------------------

def download_page(url, output_file):

    for attempt in range(retries):

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=timeout
            )

            if response.status_code == 200:

                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(response.text)

                print(f"✓ {output_file.name}")

                return True

            else:

                print(f"HTTP {response.status_code}")

        except Exception as e:

            print(e)

        time.sleep(2)

    return False


# -----------------------------------------------------
# Main
# -----------------------------------------------------

for book in config["books"]:

    book_id = book["id"]

    for volume in book["volumes"]:

        volume_id = volume["id"]

        pages = volume["pages"]

        if pages == 0:
            print(f"Skipping Volume {volume_id} (page count unknown)")
            continue

        base_url = volume["base_url"]

        output_folder = Path(
            storage_root
        ) / book_id / "raw" / f"volume{volume_id}"

        output_folder.mkdir(parents=True, exist_ok=True)

        print(f"\nDownloading Volume {volume_id}")

        for page in range(1, pages + 1):

            url = f"{base_url}/{page}"

            filename = output_folder / f"{page:04d}.html"

            if filename.exists():
                continue

            download_page(url, filename)

            time.sleep(delay)

print("\nDone.")
