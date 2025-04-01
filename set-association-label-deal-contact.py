import requests
import os

def main(event):
    # Authenticating
    oauth_token = os.getenv('your_hubspot_private_app_token')
    oauth = "Bearer " + oauth_token
    
    # Extract deal ID and contact ID from the event payload
    deal_id = event["inputFields"]["deal_id"]
    contact_id = event["inputFields"]["contact_id"]
    
    # Request headers
    headers = {
        "Authorization": oauth,
        "Content-Type": "application/json"
    }
    
    label_api_url = f"https://api.hubapi.com/crm/v4/objects/deal/{deal_id}/associations/contact/{contact_id}"
    
    # Adjusting the structure of label_data to match the API expectation
    label_data = [{
        "label": "CFF Owner",
        "name": "cff_owner",
        "maxToObjectIds": 1,
        "associationCategory": "USER_DEFINED",
        "associationTypeId": 112
    }]
    
    # Sending the request
    label_response = requests.put(label_api_url, headers=headers, json=label_data)
    
    if label_response.status_code == 204:
        print("Successfully applied the label 'CFS Owner' to the associated contact.")
    else:
        print(f"Failed to apply label: {label_response.status_code}, {label_response.text}")




