from typing import Union
from coded_flows.types import BytesIOType, Bytes, Bool, Str


coded_flows_metadata = {
    "display_name": "Download",
    "description": "Download a file",
    "type": "ui",
    "icon": "download",
    "options": [
        {
            "name": "mime",
            "display_name": "Mime Type",
            "type": "select",
            "choices": [
                "text/plain",
                "text/html",
                "text/csv",
                "application/pdf",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "application/msword",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "application/vnd.ms-excel",
                "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                "application/vnd.ms-powerpoint",
                "image/png",
                "image/jpeg",
                "image/gif",
                "application/json",
                "application/xml",
                "text/xml",
                "application/zip",
                "application/javascript",
                "text/css",
                "application/octet-stream",
            ],
            "default": "text/plain",
        }
    ],
}


def download(
    data: Union[Bytes, BytesIOType, Str],
    options,
    file_name: Str = "",
    is_disabled: Bool = False,
):
    pass
