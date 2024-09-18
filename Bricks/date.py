from coded_flows.types import Bool, Date


coded_flows_metadata = {
    "display_name": "Date",
    "description": "Date input",
    "type": "ui",
    "icon": "calendar-filled",
}


def date(
    date: Date = "",
    is_disabled: Bool = False,
) -> Date:
    return date
