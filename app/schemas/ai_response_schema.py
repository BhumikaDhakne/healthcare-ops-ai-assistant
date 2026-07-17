from pydantic import BaseModel

'''this is created so that AI response returns structured response and not random responses.
'''
class AIResponse(BaseModel):
    summary:str
    business_impact:str
    priority:str
    analysis:str
    recommended_actions:list
