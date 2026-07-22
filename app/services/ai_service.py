from app.models.event import OperationalEvent 
from app.schemas.ai_response_schema import AIResponse 
from app.prompts.user_prompt import build_user_prompt
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.exceptions import AIServiceError

import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AIService:
    def analyze_event(self, event: OperationalEvent) -> AIResponse:
        system_prompt = SYSTEM_PROMPT
        user_prompt = build_user_prompt(event)
        try:
            response = client.responses.parse(
            model= "gpt-4.1-mini",
            input= [
                {   "role": "system",
                    "content": system_prompt},
                {   "role": "user",
                    "content": user_prompt                     
                }
            ],
            text_format= AIResponse
        )
            return response.output_parsed
        except OpenAIError as e:
            raise AIServiceError("AI Services Failed") from e


    

        '''print(system_prompt) #demo
        print(user_prompt) #demo

        return AIResponse(
        summary="Demo Summary",
        business_impact="Demo Impact",
        priority="High",
        analysis="Demo Analysis",
        recommended_actions=[
            "Action 1",
        "Action 2"
    ]
)


        return AIResponse(
            summary="Member appointment scheduling issue requires timely follow-up.",
            business_impact=(
                "The delay may disrupt continuity of care, increase call-center "
                "volume, and negatively affect member satisfaction."
            ),
            priority="High",
            analysis=(
                "The reported operational issue may prevent the member from "
                "receiving the intended service within the expected timeframe. "
                "Care coordination should validate the appointment status and "
                "identify any scheduling or authorization barriers."
            ),
            recommended_actions=[
                "Contact the member to confirm the requested appointment details.",
                "Verify provider availability and any required authorization.",
                "Escalate to care coordination if an appointment cannot be scheduled promptly.",
                "Document the resolution and notify the member of the next steps.",
            ],
        )'''

