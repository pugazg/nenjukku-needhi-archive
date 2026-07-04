"""
Project constants
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"
LOGS = ROOT / "logs"
CACHE = ROOT / "cache"

USER_AGENT = (
    "Kalaignar Digital Library "
    "https://github.com/pugazg/"
)

DEFAULT_TIMEOUT = 20

DEFAULT_DELAY = 1

DEFAULT_RETRIES = 3

MAX_MISSING_PAGES = 30