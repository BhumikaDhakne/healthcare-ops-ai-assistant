from pydantic import BaseModel


class EventRequest(BaseModel):
    event_id: str
    member_id: str
    department: str
    issue: str
    event_description: str