"""
Operational Event Model

This file defines the OperationalEvent class. THIS WILL ALWAYS BE CALLED WHEN WE ARE CREATING EVENT MANUALLY,
OR ELSE THE DATA WILL COME FROM DIFFERENT SOURCES LIKE CRM, DB, ETC

THIS DOES NOT VALIDATE WHERE THE DATA IS COMING CORRECT OR NOT, THIS IS JUST A FORMAT THAT'S IT.

Purpose:
Represent a healthcare operational issue that will later be:
1. Received through an API
2. Sent to OpenAI for analysis
3. Stored in a database
4. Used to trigger automation workflows
"""


class OperationalEvent:
    """
    Represents a single healthcare operational event.
    """

    def __init__(
        self,
        event_id,
        member_id,
        department,
        issue,
        event_description,
        priority="Pending AI Analysis",
        status="Open"
    ):
        self.event_id = event_id
        self.member_id = member_id
        self.department = department
        self.issue = issue
        self.event_description = event_description
        self.priority = priority
        self.status = status