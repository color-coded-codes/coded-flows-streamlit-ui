from coded_flows.types import Number, Bool


coded_flows_metadata = {
    "display_name": "Slider",
    "description": "A numerical slider",
    "type": "ui",
    "icon": "number-123",
}


def slider(number: Number = 0, is_disabled: Bool = False) -> Number:
    return number
