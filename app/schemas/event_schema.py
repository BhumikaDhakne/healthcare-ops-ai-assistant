from pydantic import BaseModel


class EventRequest(BaseModel):
    """
    Simple request model for event data.

    This is beginner-friendly and only checks that the main event fields
    are provided as non-empty text.
    """

    event_id: str
    member_id: str
    department: str
    issue: str
    event_description: str
