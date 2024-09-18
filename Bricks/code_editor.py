from coded_flows.types import Str


coded_flows_metadata = {
    "display_name": "Code Editor",
    "description": "Code editor",
    "type": "ui",
    "icon": "code-circle-2-filled",
    "requirements": ["streamlit_code_editor"],
}


def code_editor(code: Str = "") -> Str:
    return code
