from fastapi import FastAPI
from app.models.event import OperationalEvent
from app.schemas.event_schema import EventRequest
from app.services.ai_service import AIService

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

    ai_service = AIService() #We used this to delegate work to AI service which is to analyze the operational event and provide ai responses
    ai_response = ai_service.analyze_event(operational_event)  # ai_response is a variable that is storing the response
        #we created obj ai_service and called the analyze_event fn of class AIService 
        #and provided the data which was operational_event(obj of OperationalEvent Class)


    # Return the event as JSON and we have commented this as we don't need it anymore // just kept it for knowledhe purpose
    '''return {
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
  '''
    return ai_response
    


