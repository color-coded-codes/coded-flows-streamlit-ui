from coded_flows.types import MediaData, Str, Tuple


coded_flows_metadata = {
    "display_name": "Image",
    "description": "Display an image",
    "type": "ui",
    "icon": "photo-filled",
    "options": [
        {
            "name": "channels",
            "display_name": "Channels",
            "type": "select",
            "choices": ['RGB', 'BGR'],
            "default": "RGB"
        },
        {
            "name": "output_format",
            "display_name": "Output Format",
            "type": "select",
            "choices":[
                "auto",
                "JPEG",
                "PNG",
            ],
            "default": "auto"
        },
    ],
}


def image(image: Tuple[MediaData, Str], options, caption: Str = ''):
    pass