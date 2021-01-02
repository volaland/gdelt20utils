import os

APPLICATION_NAME = "gdelt20_utils"

DATA_SOURCE = "gdelt20"

GDELT_OBJ_TYPE = ["export", "mentions", "gkg"]
GDELT_LANGUAGE = ["en", "tl"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEFAULT_DATA_DIR = ".data"
DEFAULT_DATA_PATH = os.path.join(BASE_DIR, DEFAULT_DATA_DIR)

SERIALIZATION_FORMAT = (
    "avro",
    "csv",
)
