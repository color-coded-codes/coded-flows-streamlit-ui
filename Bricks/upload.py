from coded_flows.types import BytesIOType, Bool


coded_flows_metadata = {
    "display_name": "Upload",
    "description": "Uploading a file",
    "type": "ui",
    "icon": "upload",
}


def upload(is_disabled: Bool = False) -> BytesIOType:
    uploaded_file = None
    return uploaded_file
