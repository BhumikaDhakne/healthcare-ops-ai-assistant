
def build_user_prompt(event):
    return f"""
Analyze the following healthcare operational event.

Event ID : {event.event_id}
Department : {event.department}
Issue : {event.issue}
Event Description : {event.event_description}

Based on the operational event above, provide the following:
- Summary
- Business Impact
- Priority
- Analysis
- Recommended Actions

 """
