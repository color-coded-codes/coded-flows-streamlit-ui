from coded_flows.types import Bool


coded_flows_metadata = {
    "display_name": "Button",
    "description": "Action button",
    "type": "ui",
    "icon": "hand-click",
}


def button(is_disabled: Bool = False) -> Bool:
    clicked = False
    return clicked
