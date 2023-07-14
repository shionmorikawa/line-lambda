import os
import requests
import json

class TimeTree:
    CALENDER_ID = os.getenv('TIMETREE_CALENDER_ID')
    MY_USER_ID = os.getenv('TIMETREE_MY_USER_ID')
    LABEL_ID = os.getenv('TIMETREE_LABEL_ID')
    ACCESS_TOKEN = os.getenv('TIMETREE_ACCESS_TOKEN')
    API_URL = "https://timetreeapis.com/calendars/{}/events".format(
        CALENDER_ID)

    @classmethod
    def create_schedule(cls, title, description, start_at, end_at):
        request_data = {
            "data": {
                "attributes": {
                    "category": "schedule",
                    "title": title,
                    "description": description,
                    "all_day": "false",
                    "start_at": start_at,
                    "end_at": end_at,
                    "start_timezone": "Asia/Tokyo",
                    "end_timezone": "Asia/Tokyo",
                },
                "relationships": {
                    "label": {
                        "data": {
                            "id": cls.LABEL_ID,
                            "type": "label"
                        }
                    },
                    "attendees": {
                        "data": [
                            {"id": cls.MY_USER_ID, "type": "user"}
                        ]
                    }
                }
            }
        }

        headers = {
            'Accept': 'application/vnd.timetree.v1+json',
            'Authorization': f'Bearer {cls.ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }

        response = requests.post(
            cls.API_URL, headers=headers, data=json.dumps(request_data))

        if response.status_code == 200:
            print('Event created successfully')
            return "OK"
        else:
            print('Failed to create event. Status code:', response.status_code)
            print(response.text)
            return response.status_code
