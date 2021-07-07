import os
from pathlib import Path
from typing import List

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

# ------------------------------------------------------------------------------------------------------------
# Application
# ------------------------------------------------------------------------------------------------------------
VERSION = "0.1.0"

DEBUG: bool = config("DEBUG", cast=bool, default=os.getenv("DEBUG", False))

BASE_DIR = config("BASE_DIR", default=os.getenv("BASE_DIR", Path(__file__).parent.parent.parent))

PROJECT_NAME = config("PROJECT_NAME", default=os.getenv("PROJECT_NAME", "domain-service"))

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=os.getenv("ALLOWED_HOSTS")
)
