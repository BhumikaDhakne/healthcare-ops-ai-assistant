from fastapi import FastAPI
from app.models.event import OperationalEvent
from app.schemas.event_schema import EventRequest

# Create the FastAPI application
app = FastAPI(
    title="Healthcare Operations AI Assistant",
    description="First API for receiving healthcare operational events.",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Healthcare Operations AI Assistant is running!"
    }


@app.post("/operational-events")
def create_event(event: EventRequest):

    # Create an OperationalEvent object
    operational_event = OperationalEvent(
        event_id=event.event_id,
        member_id=event.member_id,
        department=event.department,
        issue=event.issue,
        event_description=event.event_description
    )

    # Return the event as JSON
    return {
        "message": "Event received successfully",
        "event": {
            "event_id": operational_event.event_id,
            "member_id": operational_event.member_id,
            "department": operational_event.department,
            "issue": operational_event.issue,
            "event_description": operational_event.event_description,
            "priority": operational_event.priority,
            "status": operational_event.status
        }
    }