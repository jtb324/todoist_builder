# Todoist Builder CLI:

## Purpose of this project:

The purpose of this project is to create a python script that interacts with the Todoist api and can add due dates from my classes schedule, which is an xlsx, to my todo list. Basically I am just lazy and don't want to have to make 50 or so individual task by hand.

## Current Scripts:

- **Read_calendar**: This is the script with the CLI interface code and the class Calendar_xlsx for reading in the calendar document and then getting interacting with the api.

## Current Progress:

- At the moment, all the script does is load the provided xlsx sheet into a pandas dataframe and then use the api key to get all projects if the user passed the correct argument.
