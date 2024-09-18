from typing import Union
from coded_flows.types import BytesIOType


coded_flows_metadata = {
    "display_name": "Camera",
    "description": "Camera input",
    "type": "ui",
    "icon": "device-computer-camera",
}


def camera() -> BytesIOType:
    image = None
    return image
