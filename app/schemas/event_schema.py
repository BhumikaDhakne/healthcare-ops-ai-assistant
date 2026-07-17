from pydantic import BaseModel


class EventRequest(BaseModel):
    """
    Request model for creating a healthcare operational event.

    This is beginner-friendly and only checks that the main event fields
    are provided as non-empty text.

    ONLY RESPONSIBILITY IS TO VALIDATE INCOMING REQUEST, 
    THIS WILL NOT BE USED TO CREATE A OPERATIONAL EVENT FOR THAT EVENT.PY(OPERATIONALEVENT) WILL BE USED

    THIS WILL BE USED BY FAST API ONLY TO VALIDATE THE INCOMING REQUESTS
    """

    event_id: str
    member_id: str
    department: str
    issue: str
    event_description: str
