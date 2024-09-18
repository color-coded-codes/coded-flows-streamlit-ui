from coded_flows.types import Number, Bool


coded_flows_metadata = {
    "display_name": "Number Input",
    "description": "A numerical input",
    "type": "ui",
    "icon": "number-123",
}


def number_input(number: Number = 0, is_disabled: Bool = False) -> Number:
    return number
