from models.event import OperationalEvent

# Event 1
event_1 = OperationalEvent(
    event_id="EVT001",
    member_id="MEM1001",
    department="Lab",
    issue="Sample Collection Delay",
    event_description="No one came for sample collection. Member has been fasting since morning."
)

# Event 2
event_2 = OperationalEvent(
    event_id="EVT002",
    member_id="MEM1002",
    department="Pharmacy",
    issue="Medicine Out of Stock",
    event_description="Requested medicine is currently unavailable."
)

# Event 3
event_3 = OperationalEvent(
    event_id="EVT003",
    member_id="MEM1003",
    department="OPD",
    issue="Cashless Denied",
    event_description="Hospital denied cashless consultation for the member."
)


events = [event_1, event_2, event_3]


for event in events:
    print("----------------------------")
    print(f"Event ID      : {event.event_id}")
    print(f"Member ID     : {event.member_id}")
    print(f"Department    : {event.department}")
    print(f"Issue         : {event.issue}")
    print(f"Description   : {event.event_description}")
    print(f"Priority      : {event.priority}")
    print(f"Status        : {event.status}")