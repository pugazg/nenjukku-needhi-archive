"""
Kalaignar Digital Library
Volume Builder

Part 1 - Foundation

Responsibilities
----------------
✓ Load config.yaml
✓ Locate cleaned pages
✓ Create output folder
✓ Read markdown pages
✓ Metadata helpers

Merging begins in Part 2.
"""

from pathlib import Path
import yaml
import re


class VolumeBuilder:

    ####################################################################
    # Initialization
    ####################################################################

    def __init__(self, config_file="config.yaml"):

        self.root = Path.cwd()

        with open(config_file, encoding="utf-8") as f:

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

        print(f"Book    : {self.book['title']}")
        print(f"Author  : {self.book['author']}")
        print(f"Volumes : {len(self.volumes)}")

        print("=" * 70)

    ####################################################################
    # Folder Helpers
    ####################################################################

    def cleaned_folder(self, volume):

        return Path(

            str(volume["output"]).replace(

                "/raw/",

                "/cleaned/"

            )

        )

    ####################################################################

    def output_folder(self):

        folder = Path(

            "output/markdown"

        )

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        return folder

    ####################################################################
    # Files
    ####################################################################

    def markdown_files(self, volume):

        folder = self.cleaned_folder(volume)

        return sorted(

            folder.glob("*.md")

        )

    ####################################################################

    def output_file(self, volume):

        return self.output_folder() / f"volume{volume['id']}.md"

    ####################################################################
    # Reader
    ####################################################################

    def read_markdown(self, file):

        return file.read_text(

            encoding="utf-8",

            errors="ignore"

        )
        ####################################################################
    # Split Markdown
    ####################################################################

    def split_markdown(self, markdown):

        if not markdown.startswith("---"):
            return "", markdown

        parts = markdown.split("---", 2)

        if len(parts) < 3:
            return "", markdown

        frontmatter = "---" + parts[1] + "---"

        body = parts[2].lstrip()

        return frontmatter, body
        ####################################################################
    # Page Number
    ####################################################################

    def page_number(self, md_file):

        return int(md_file.stem)
        ####################################################################
    # Clean Page Body
    ####################################################################

    def clean_body(self, body):

        body = body.strip()

        body = re.sub(

            r"\n{3,}",

            "\n\n",

            body

        )

        return body
        ####################################################################
    # Build One Page
    ####################################################################

    def build_page(self, md_file):

        markdown = self.read_markdown(md_file)

        _, body = self.split_markdown(markdown)

        body = self.clean_body(body)

        page = self.page_number(md_file)

        result = []

        result.append("")

        result.append(f"<!-- PAGE {page:04} -->")

        result.append("")

        result.append(body)

        result.append("")

        return "\n".join(result)
        ####################################################################
    # Volume Header
    ####################################################################

    def build_header(self, volume):

        return f"""# {self.book['title']}

## {volume['title']}

Author: {self.book['author']}

---

"""
        ####################################################################
    # Merge All Pages
    ####################################################################

    def merge_volume(self, volume):

        pages = []

        pages.append(

            self.build_header(volume)

        )

        files = self.markdown_files(volume)

        for md_file in files:

            pages.append(

                self.build_page(md_file)

            )

        return "\n".join(pages)
        ####################################################################
    # Write Volume
    ####################################################################

    def write_volume(self, volume, text):

        output = self.output_file(volume)

        output.write_text(

            text,

            encoding="utf-8"

        )

        return output
        ####################################################################
    # Build One Volume
    ####################################################################

    def build_volume(self, volume):

        print()

        print("=" * 70)
        print(volume["title"])
        print("=" * 70)

        files = self.markdown_files(volume)

        print(f"Pages : {len(files)}")

        text = self.merge_volume(volume)

        output = self.write_volume(

            volume,

            text

        )

        print()

        print(f"Saved : {output}")
        ####################################################################
    # Run
    ####################################################################

    def run(self):

        self.print_summary()

        print()

        for volume in self.volumes:

            self.build_volume(volume)

        print()

        print("=" * 70)
        print("Volume Building Complete")
        print("=" * 70)
###############################################################
# Entry Point
###############################################################

def main():

    builder = VolumeBuilder()

    builder.run()


if __name__ == "__main__":

    main()