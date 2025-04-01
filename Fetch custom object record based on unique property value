
import requests
import os
import json

def main(event):
    oauth_token = os.getenv('your_hubspot_private_app_key')
    oauth = "Bearer " + oauth_token
    
    short_code = event["inputFields"]["short_code"]

    # Define the body for the request
    data = {
        "filterGroups": [
            {
                "filters": [
                    {
                        "propertyName": "warehouse_short_code",
                        "operator": "EQ",
                        "value": short_code  # Using the short_code variable directly
                    }
                ]
            }
        ],
        "properties": [
            "partner_manager_slack_id"
        ]
    }
    
    # HubSpot API endpoint for retrieving deals with specific properties
    get_api_url = "https://api.hubapi.com/crm/v3/objects/2-8214323/search"
    
    # Sending a POST request to retrieve the deal properties
    headers = {
        "Authorization": oauth,
        "Content-Type": "application/json"
    }
    
    # Make the request and handle the response
    response = requests.post(get_api_url, headers=headers, json=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract data from response to populate output fields
        response_data = response.json()
        output_fields = {
            "partner_manager_slack_id": response_data.get("results", [{}])[0].get("properties", {}).get("partner_manager_slack_id")
        }
    else:
        # If there was an error, set output_fields to show the error
        output_fields = {
            "error": response.status_code,
            "message": response.text
        }
    
    return {
        "outputFields": output_fields
    }


