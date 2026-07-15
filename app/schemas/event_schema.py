from pydantic import BaseModel


class EventRequest(BaseModel):
    """
    Request model for creating a healthcare operational event.

    This is beginner-friendly and only checks that the main event fields
    are provided as non-empty text.
    """

    event_id: str
    member_id: str
    department: str
    issue: str
    event_description: str
