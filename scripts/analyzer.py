"""
Kalaignar Digital Library
Book Analyzer

Part 1 - Foundation

Responsibilities
----------------
✓ Load config.yaml
✓ Read merged volume markdown
✓ Create analysis folder
✓ Save JSON reports
✓ Volume helpers

Actual analysis begins in Part 2.
"""

from pathlib import Path
import json
import yaml
import re


class Analyzer:

    ####################################################################
    # Initialization
    ####################################################################

    def __init__(self, config_file="config.yaml"):

        self.root = Path.cwd()

        self.config_path = self.root / config_file

        if not self.config_path.exists():
            raise FileNotFoundError(self.config_path)

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

        print(f"Book    : {self.book['title']}")
        print(f"Author  : {self.book['author']}")
        print(f"Volumes : {len(self.volumes)}")

        print("=" * 70)

    ####################################################################
    # Files
    ####################################################################

    def volume_file(self, volume):

        return Path(

            "output/markdown"

        ) / f"volume{volume['id']}.md"

    ####################################################################

    def analysis_folder(self):

        folder = Path(

            "output/analysis"

        )

        folder.mkdir(

            parents=True,

            exist_ok=True

        )

        return folder

    ####################################################################

    def report_file(self, volume):

        return self.analysis_folder() / f"volume{volume['id']}.json"

    ####################################################################
    # Reader
    ####################################################################

    def read_volume(self, volume):

        return self.volume_file(volume).read_text(

            encoding="utf-8",

            errors="ignore"

        )

    ####################################################################
    # Writer
    ####################################################################

    def save_report(self, volume, report):

        with open(

            self.report_file(volume),

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                report,

                f,

                ensure_ascii=False,

                indent=2

            )
        ####################################################################
    # Split Volume into Pages
    ####################################################################

    def split_pages(self, text):

        pattern = r"<!-- PAGE (\d{4}) -->"

        parts = re.split(pattern, text)

        pages = []

        #
        # parts =
        # [before,
        #  page,
        #  text,
        #  page,
        #  text,
        #  ...]
        #

        for i in range(1, len(parts), 2):

            page = int(parts[i])

            body = parts[i + 1].strip()

            pages.append({

                "page": page,

                "text": body

            })

        return pages
        ####################################################################
    # Heading Detection
    ####################################################################

    def detect_heading(self, text):

        lines = [

            line.strip()

            for line in text.splitlines()

            if line.strip()

        ]

        if not lines:

            return None

        #
        # Ignore markdown headings
        #

        while lines and lines[0].startswith("#"):

            lines.pop(0)

        if not lines:

            return None

        heading = lines[0]

        #
        # Ignore very long lines
        #

        if len(heading) > 60:

            return None

        #
        # Ignore obvious publisher metadata
        #

        ignore = [

            "Author",

            "முதற் பதிப்பு",

            "திருமகள்",

            "உரிமை",

            "விலை",

            "Paper",

            "Binding"

        ]

        for item in ignore:

            if heading.startswith(item):

                return None

        return heading
        ####################################################################
    # Analyze One Page
    ####################################################################

    def analyze_page(self, page):

        heading = self.detect_heading(

            page["text"]

        )

        return {

            "page": page["page"],

            "heading": heading,

            "length": len(page["text"])

        }
        ####################################################################
    # Analyze Volume
    ####################################################################

    def analyze_volume(self, volume):

        print()

        print("=" * 70)

        print(volume["title"])

        print("=" * 70)

        text = self.read_volume(volume)

        pages = self.split_pages(text)

        report = {

            "book": self.book["title"],

            "volume": volume["id"],

            "pages": [],

            "statistics": {}

        }

        for page in pages:

            report["pages"].append(

                self.analyze_page(page)

            )

        report["statistics"] = {

            "page_count": len(pages),

            "character_count": len(text)

        }

        self.save_report(

            volume,

            report

        )

        print(

            f"Pages : {len(pages)}"

        )

        print(

            f"Report: {self.report_file(volume)}"

        )
        ####################################################################
    # Run
    ####################################################################

    def run(self):

        self.print_summary()

        for volume in self.volumes:

            self.analyze_volume(volume)

        print()

        print("=" * 70)

        print("Analysis Complete")

        print("=" * 70)

###############################################################
# Entry Point
###############################################################

def main():

    analyzer = Analyzer()

    analyzer.run()


if __name__ == "__main__":

    main()