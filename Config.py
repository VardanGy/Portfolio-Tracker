import tomllib
from pathlib import Path

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

TRANSACTIONS_FILE = Path(config["paths"]["transactions_file"])
DECIMALS = int(config["display"]["decimals"])
CURRENCY = config["display"]["currency"]