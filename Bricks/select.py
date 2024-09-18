from coded_flows.types import Iterable, Bool, Int, Any


coded_flows_metadata = {
    "display_name": "Select",
    "description": "Select an option from a list of choices",
    "type": "ui",
    "icon": "select",
}


def select(choices: Iterable = [], index: Int = 0, is_disabled: Bool = False) -> Any:
    selection = None
    return selection
