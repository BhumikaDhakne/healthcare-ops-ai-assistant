# Operational Event Design

## Purpose

An **Operational Event** represents a single business event occurring within healthcare operations that may require AI analysis, recommendations, prioritization, or workflow automation.

The Operational Event serves as the core business entity of the application. Every AI analysis begins with an operational event.

---

## Example Operational Events

- Vision order partially delivered due to item unavailability.
- Vision order not delivered because the requested item is out of stock.
- Dental treatment materials are unavailable at the clinic.
- Member requests appointment rescheduling because the hospital requires a cashless approval letter.
- Hospital cancels an appointment because the doctor is unavailable.
- Hospital denies a cashless appointment request.
- Sample collection executive did not arrive, while the member has been fasting since morning.
- Laboratory reports are delayed or only partially available.
- Vaccine has not been delivered to the requested vaccination center.
- Medicines are delayed beyond the expected delivery timeline.
- Medicine order is rejected because the requested medicine is out of stock.

---

# Candidate Mandatory Fields

> **Note:** These fields are intentionally left blank and will be finalized during the backend design phase after understanding the complete business requirements.

| Field | Why is it Required? |
|--------|---------------------|
| TBD | To be determined during model design. |

---

# Fields Hidden From AI

The following fields should **not** be shared with the LLM because they do not contribute to business reasoning and may expose unnecessary internal information.

| Field | Why should AI not receive it? |
|--------|-------------------------------|
| Internal Database ID | Used only for internal database references. |
| Created By User ID | Internal audit information with no business value. |
| Updated By | Audit trail only. |
| API Keys / Secrets | Sensitive system credentials. |
| Internal System Logs | Technical logs that add noise without improving AI reasoning. |

---

# Open Questions

The following design decisions will be answered before implementing the `OperationalEvent` model.

- Should an operational event belong to exactly one department?
- Can a single operational event involve multiple departments?
- Should priority be provided by the source system or inferred by the AI?
- Should the AI receive raw operational comments or cleaned and standardized comments?
- Should historical events related to the same order or member be provided as additional context for better AI reasoning?

---

# Notes

The objective of this document is **not** to design the Python class.

The objective is to understand the business information required to represent an operational event before deciding:

- the backend model,
- the API schema,
- the AI prompt,
- and the overall application architecture.
