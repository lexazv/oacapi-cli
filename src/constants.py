from enum import Enum, auto

DEFAULT_OBJECT = "catalog"
QUERY_BASE = "https://api.{catalog}.space/"


class Catalog(Enum):
    """Available catalog names.
    """
    ASTROCATS = auto()
    SNE = auto()
    TDE = auto()
    KILONOVA = auto()
    FASTSTARS = auto()


class OutputFormat(Enum):
    """Available output formats.
    """
    JSON = auto()
    CSV = auto()
    TSV = auto()
