from coded_flows.types import Bool


coded_flows_metadata = {
    "display_name": "Toggle",
    "description": "Activating a toggle",
    "type": "ui",
    "icon": "toggle-right",
}


def checkbox(toggled: Bool = False, is_disabled: Bool = False) -> Bool:
    return toggled
