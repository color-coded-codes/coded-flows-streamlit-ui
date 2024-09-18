from coded_flows.types import Str, Bool


coded_flows_metadata = {
    "display_name": "Textarea",
    "description": "A long textual input",
    "type": "ui",
    "icon": "typography",
}


def textarea_input(text: Str = "", is_disabled: Bool = False) -> Str:
    return text
