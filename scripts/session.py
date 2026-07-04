import requests

from .constants import USER_AGENT


def create_session():

    session = requests.Session()

    session.headers.update({

        "User-Agent": USER_AGENT

    })

    return session