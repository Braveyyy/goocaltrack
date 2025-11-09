import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPE = "https://www.googleapis.com/auth/calendar"
# See, edit, share, and permanently delete all the calendars you can access using Google Calendar.

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPE)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPE
            )
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

    try:
        startTimer = input("Enter START to begin timer: ")
        if startTimer == "START":
            initialTime = datetime.datetime.now().isoformat() # isoformat string: 'YYYY-MM-DD HH:MM:SS.mmmmmm'
            while input():
                print("timing")
            print("timer ended")
            endTime = datetime.datetime.now().isoformat()
        #print("INITIAL TIME: ", initialTime)
        #print("END TIME: ", endTime)
        event = {
            'summary': 'TEST SUMMARY',
            'description': 'TEST DESC',
            'start': {
                'dateTime': initialTime,
                'timeZone': 'US/Mountain',
            },
            'end': {
                'dateTime': endTime,
                'timeZone': 'US/Mountain',
            }
        }
        service = build("calendar", "v3", credentials=creds)
        service.events().insert(calendarId='primary', body=event).execute()
        
    except HttpError as error:
        print(f"An error occurred: {error}")    


if __name__ == '__main__':
    main()