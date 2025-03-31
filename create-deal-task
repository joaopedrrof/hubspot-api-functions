import requests
import os

def main(event):
    # Authenticating
    oauth_token = os.getenv('privateAppKeyHere') # Your HubSpot's private app variable name created on the fields mapping section
    oauth = "Bearer " + oauth_token
    
    # Deal ID
    deal_id = 18728352607
    
    # Task data
    task_data = {
        "properties": {
            "hs_timestamp": {{Define the timestamp date accordingly to context}},
            "hs_task_subject": "Follow-up for John Smith",
            "hs_task_body": "Send Proposal",
            "hubspot_owner_id": "{{HubSpot Owner's ID}}",
            "hs_task_status": "WAITING",
            "hs_task_priority": "HIGH",
            "hs_task_type":"TODO"
        },
        "associations": [
            {
                "to": {
                  "id": {{map deal id dynamically}}
                },
                "types": [
                    {
                        "associationCategory": "HUBSPOT_DEFINED",
                        "associationTypeId": 216 # Deal to task association type
                    }
                ]
            }
        ]
    }
    
    # Making the request
    headers = {
        "Authorization": oauth,
        "Content-Type": "application/json"
    }
    url = "https://api.hubapi.com/crm/v3/objects/tasks"
    response = requests.post(url, headers=headers, json=task_data)
    
    if response.status_code == 201:
        print("Task created successfully.")
    else:
        print("Failed to create task:", response.status_code)
