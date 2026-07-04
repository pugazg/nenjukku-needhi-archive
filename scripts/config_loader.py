from pathlib import Path
import yaml


ROOT = Path(__file__).resolve().parent.parent


CONFIG = ROOT / "config.yaml"


def load_config():

    with open(CONFIG, encoding="utf-8") as f:

        return yaml.safe_load(f)