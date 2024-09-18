from coded_flows.types import Bool


coded_flows_metadata = {
    "display_name": "Checkbox",
    "description": "Checking a box",
    "type": "ui",
    "icon": "checkbox",
}


def checkbox(checked: Bool = False, is_disabled: Bool = False) -> Bool:
    return checked
