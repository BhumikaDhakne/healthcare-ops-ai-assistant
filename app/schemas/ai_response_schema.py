from pydantic import BaseModel


class AIResponse(BaseModel):
    summary:str
    business_impact:str
    priority:str
    analysis:str
    recommended_actions:list
