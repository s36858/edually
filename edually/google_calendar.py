from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from datetime import timedelta, datetime
import pytz


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def credentials():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def get_events(number):
    creds = credentials()
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming %s events' % number)
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=number, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


def create_event(start_date, start_time, title, description, length, reminderMinutes):
    creds = credentials()
    service = build('calendar', 'v3', credentials=creds)
    start_time = datetime.strptime(
        str(start_time), '%H:%M:%S') - timedelta(hours=2, minutes=0)
    start_datetime = datetime.combine(start_date,
                                      datetime.time(start_time)).replace(tzinfo=pytz.UTC)
    event = (
        service.events()
        .insert(
            calendarId="primary",
            body={
                "summary": title,
                "description": description,
                "start": {"dateTime": start_datetime.isoformat()},
                "end": {
                    "dateTime": (start_datetime + timedelta(minutes=length)).isoformat()
                },
                "reminders": {
                    "useDefault": "false",
                    "overrides": [
                        {
                            "method": "email", "minutes": reminderMinutes
                        },
                        {"method": "popup", "minutes": reminderMinutes},
                    ]
                }
            },
        )
        .execute()
    )

    print(event)
