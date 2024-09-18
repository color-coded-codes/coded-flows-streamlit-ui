from coded_flows.types import Str, Bool


coded_flows_metadata = {
    "display_name": "Text Input",
    "description": "A textual input",
    "type": "ui",
    "icon": "typography",
}


def text_input(text: Str = "", is_disabled: Bool = False) -> Str:
    return text
