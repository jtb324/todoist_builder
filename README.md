# Todoist Builder CLI:

## Purpose of this project:

The purpose of this project is to create a python script that interacts with the Todoist api and can add due dates from my classes schedule, which is an xlsx, to my todo list. Basically I am just lazy and don't want to have to make 50 or so individual task by hand.

## Current Scripts:

- **Read_calendar**: This is the script with the CLI interface code and the class Calendar_xlsx for reading in the calendar document and then getting interacting with the api.

  - _all useful flags_:
    -c: This is the calendar page
    -k: This is the users api page
    -flp: This flag will generate a json of all of the user's projects
    -ct: This flag will create a new task for each due date in the passed calendar

## Current Progress:

- The CLI has the ability to list all current projects when True is passed to teh -flp flag and the CLI can add all the due dates from the calendar if the -ct is set to true. Currently is only set for the specific project that I had in mind. It uses the id number to identify the project which would be hard for the user to specify if they don't know it off the top of their head
