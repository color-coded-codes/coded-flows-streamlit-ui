from coded_flows.types import Bool, Time


coded_flows_metadata = {
    "display_name": "Time",
    "description": "Time input",
    "type": "ui",
    "icon": "clock-filled",
}


def time(
    time: Time = "",
    is_disabled: Bool = False,
) -> Time:
    return time
