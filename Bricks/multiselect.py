from coded_flows.types import Iterable, Bool, List


coded_flows_metadata = {
    "display_name": "Multiselect",
    "description": "Select multiple options from a list of choices",
    "type": "ui",
    "icon": "select",
}


def multiselect(
    choices: Iterable = [], default: Iterable = [], is_disabled: Bool = False
) -> List:
    selections = None
    return selections
