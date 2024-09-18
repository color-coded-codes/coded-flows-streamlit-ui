from coded_flows.types import DataFrame


coded_flows_metadata = {
    "display_name": "Line Chart",
    "description": "Line chart display",
    "type": "ui",
    "icon": "chart-line",
    "options": [
        {
            "name": "x",
            "display_name": "X axis attribute",
            "type": "input",
            "max_characters": 50,
        },
        {
            "name": "y",
            "display_name": "Y axis attribute",
            "type": "input",
            "max_characters": 50,
        },
        {
            "name": "color",
            "display_name": "Color attribute",
            "type": "input",
            "max_characters": 50,
        },
    ],
}


def line_chart(data: DataFrame, options):
    pass
