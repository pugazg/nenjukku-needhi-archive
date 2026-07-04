from pathlib import Path


def ensure_directory(path):

    Path(path).mkdir(

        parents=True,

        exist_ok=True

    )


def html_filename(output, page):

    return Path(output) / f"{page:04d}.html"


def page_exists(output, page):

    return html_filename(output, page).exists()
