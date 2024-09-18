from typing import Union
from coded_flows.types import MediaData, Str


coded_flows_metadata = {
    "display_name": "Video",
    "description": "Display a video",
    "type": "ui",
    "icon": "video",
    "options": [
        {
            "name": "format",
            "display_name": "Format",
            "type": "select",
            "choices": [
                "video/mp4",
                "video/webm",
                "video/ogg",
            ],
            "default": "video/mp4",
        }
    ],
}


def video(video: Union[MediaData, Str], options):
    pass
