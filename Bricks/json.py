from typing import Union
from coded_flows.types import Str, Dict, List, DataDict, DataRecords


coded_flows_metadata = {
    "display_name": "JSON",
    "description": "Json display",
    "type": "ui",
    "icon": "json",
}


def json(body: Union[Str, Dict, List, DataDict, DataRecords]):
    pass
