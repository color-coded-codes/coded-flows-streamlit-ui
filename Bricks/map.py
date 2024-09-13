from coded_flows.types import DataFrame


coded_flows_metadata = {
    "display_name": "Map",
    "description": "Display a map",
    "type": "ui",
    "icon": "map",
    "options": [
        {
            "name": "size",
            "display_name": "Size Attribute",
            "type": "input",
            "max_characters": 50
        },
        {
            "name": "color",
            "display_name": "Color Attribute",
            "type": "input",
            "max_characters": 50
        }
    ],
}


def map(data: DataFrame, options):
    pass