"""
Kalaignar Digital Library
Cleaning Engine

Part 1 - Foundation

Responsibilities
----------------
✓ Load config.yaml
✓ Read extracted markdown
✓ Create cleaned folders
✓ Resume support
✓ Metadata helpers

Cleaning rules begin in Part 2.
"""

from pathlib import Path
import json
import yaml
import re
import unicodedata


class Cleaner:

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

    def extracted_folder(self, volume):

        return Path(

            str(volume["output"]).replace(

                "/raw/",

                "/extracted/"

            )

        )

    ####################################################################

    def cleaned_folder(self, volume):

        folder = Path(

            str(volume["output"]).replace(

                "/raw/",

                "/cleaned/"

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

    def markdown_files(self, volume):

        folder = self.extracted_folder(volume)

        return sorted(

            folder.glob("*.md")

        )

    ####################################################################

    def output_file(self, volume, md_file):

        return self.cleaned_folder(volume) / md_file.name

    ####################################################################

    def metadata_file(self, volume):

        return self.cleaned_folder(volume) / "metadata.json"

    ####################################################################

    def already_cleaned(self, volume, md_file):

        return self.output_file(

            volume,

            md_file

        ).exists()

    ####################################################################
    # Read / Write
    ####################################################################

    def read_markdown(self, md_file):

        return md_file.read_text(

            encoding="utf-8",

            errors="ignore"

        )

    ####################################################################

    def write_markdown(

        self,

        volume,

        md_file,

        text

    ):

        output = self.output_file(

            volume,

            md_file

        )

        output.write_text(

            text,

            encoding="utf-8"

        )

    ####################################################################
    # Metadata
    ####################################################################

    def save_metadata(

        self,

        volume,

        metadata

    ):

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
    # Markdown Parser
    ####################################################################

    def split_markdown(self, markdown):

        if not markdown.startswith("---"):
            return "", markdown

        parts = markdown.split("---", 2)

        if len(parts) < 3:
            return "", markdown

        frontmatter = "---" + parts[1] + "---\n\n"

        body = parts[2].lstrip()

        return frontmatter, body
        ####################################################################
    # Unicode Normalization
    ####################################################################

    def normalize_unicode(self, text):

        return unicodedata.normalize(

            "NFC",

            text

        )
        ####################################################################
    # Remove Standalone Page Numbers
    ####################################################################

    def remove_page_numbers(self, text):

        cleaned = []

        for line in text.splitlines():

            line = line.strip()

            if re.fullmatch(r"\d+", line):
                continue

            cleaned.append(line)

        return "\n".join(cleaned)
        ####################################################################
    # Collapse Empty Lines
    ####################################################################

    def collapse_blank_lines(self, text):

        text = re.sub(

            r"\n{3,}",

            "\n\n",

            text

        )

        return text.strip()
        ####################################################################
    # Join Broken Tamil Letters
    ####################################################################

    def join_broken_letters(self, text):

        lines = text.splitlines()

        result = []

        i = 0

        while i < len(lines):

            line = lines[i].rstrip()

            #
            # Single Tamil character on its own line
            #

            if (

                len(line) == 1

                and i + 1 < len(lines)

                and lines[i + 1]

            ):

                result.append(

                    line + lines[i + 1].lstrip()

                )

                i += 2

                continue

            result.append(line)

            i += 1

        return "\n".join(result)
        ####################################################################
    # Typography Cleanup
    ####################################################################

    def typography_cleanup(self, text):

        replacements = {

            "“": '"',

            "”": '"',

            "‘": "'",

            "’": "'",

            "–": "-",

            "—": "-",

            "…": "...",

            "\u00a0": " "

        }

        for old, new in replacements.items():

            text = text.replace(

                old,

                new

            )

        return text
        ####################################################################
    # Master Cleaning Pipeline
    ####################################################################

    def clean_text(self, markdown):

        frontmatter, body = self.split_markdown(

            markdown

        )

        body = self.normalize_unicode(body)

        body = self.remove_page_numbers(body)

        body = self.join_broken_letters(body)

        body = self.typography_cleanup(body)

        body = self.collapse_blank_lines(body)

        return frontmatter + body + "\n"
        ####################################################################
    # Process One Page
    ####################################################################

    def process_page(self, volume, md_file):

        #
        # Resume support
        #

        if self.already_cleaned(volume, md_file):

            return "skipped"

        markdown = self.read_markdown(md_file)

        cleaned = self.clean_text(markdown)

        self.write_markdown(

            volume,

            md_file,

            cleaned

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

        files = self.markdown_files(volume)

        total = len(files)

        print(f"Pages found : {total}")

        cleaned = 0
        skipped = 0

        for index, md_file in enumerate(files, start=1):

            result = self.process_page(

                volume,

                md_file

            )

            if result == "done":
                cleaned += 1

            else:
                skipped += 1

            if index % 25 == 0 or index == total:

                print(

                    f"{index}/{total} pages processed"

                )

        metadata = {

            "book": self.book["title"],

            "volume": volume["id"],

            "title": volume["title"],

            "pages": total,

            "cleaned": cleaned,

            "skipped": skipped

        }

        self.save_metadata(

            volume,

            metadata

        )

        print()

        print("Finished")

        print(metadata)
        ####################################################################
    # Run Cleaner
    ####################################################################

    def run(self):

        self.print_summary()

        print()

        for volume in self.volumes:

            self.process_volume(

                volume

            )

        print()

        print("=" * 70)
        print("Cleaning Complete")
        print("=" * 70)
###############################################################
# Entry Point
###############################################################

def main():

    cleaner = Cleaner()

    cleaner.run()


if __name__ == "__main__":

    main()
    