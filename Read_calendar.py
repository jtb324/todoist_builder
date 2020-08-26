import pandas as pd
import numpy as np
from todoist.api import TodoistAPI
import argparse

# import calendar into pandas df


class Calendar_xlxs:

    def __init__(self, calendar_path: str, apikey: str):
        self.calendar = pd.read_excel(
            calendar_path, header=None, skiprows=4, usecols=[0, 1, 2, 3, 4], names=["Month", "Date", "Weekday", "Topic", "Reading Assignment"])

        print(self.calendar)

        self.apikey = apikey

    def get_all_projects(self):

        api = TodoistAPI(self.apikey)

        api.sync()

        print(api.state["projects"])


def run(args):

    calendar_handler = Calendar_xlxs(args.cal, args.api)

    if args.flp:

        calendar_handler.get_all_projects()


def main():
    parser = argparse.ArgumentParser(
        description="")

    parser.add_argument("-c", "--calendar", help="This argument takes the path to the calendar excel sheet",
                        dest="cal", type=str, required=True)

    parser.add_argument("-k", "--api", help="This argument takes the users api key",
                        dest="api", type=str, required=True)

    parser.add_argument("-flp", help="This argument will print a full list of projects if set to true",
                        dest="flp", type=bool, required=False, default=False)

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
