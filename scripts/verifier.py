from bs4 import BeautifulSoup


def is_valid_page(html):

    if html is None:

        return False

    soup = BeautifulSoup(

        html,

        "lxml"

    )

    content = soup.find(

        "div",

        class_="mw-parser-output"

    )

    if content is None:

        return False

    text = content.get_text(

        strip=True

    )

    return len(text) > 50