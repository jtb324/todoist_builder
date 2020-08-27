import pandas as pd
import numpy as np
from todoist.api import TodoistAPI
import argparse
import datetime

# import calendar into pandas df


class Calendar_xlxs:

    def __init__(self, calendar_path: str, apikey: str):
        self.calendar = pd.read_excel(
            calendar_path, header=None, skiprows=4, usecols=[0, 1, 2, 3, 4], names=["Month", "Date", "Weekday", "Topic", "Reading Assignment"])

        self.apikey = apikey

        print(self.calendar)

        self.project_name = 2241251289
        self.cur_year = datetime.datetime.now().year
        self.cur_month = datetime.datetime.now().strftime("%B")
        self.cur_day = datetime.datetime.now().day

    def get_all_projects(self):

        api = TodoistAPI(self.apikey)

        api.sync()

        print(api.state["projects"])

    def create_task(self):
        print("Creating the new task ...")

        api = TodoistAPI(self.apikey)

        api.sync()

        # get a starting month
        for row in self.calendar.itertuples():
            # 0 index = tuple index
            # 1 index = Month
            # 2 index = Date
            # 3 index = Weekday
            # 4 index = Topic
            # 5 index = Reading Assignment
            month = row[1]

            try:
                prior_month

            except NameError:
                prior_month = None

            try:

                not_num = float(row[1])
                is_nan = np.isnan(not_num)

            except ValueError:

                is_nan = False

            if is_nan or row[1] == " ":
                month = prior_month

            prior_month = month

            # get the date
            date = row[2]

            try:

                not_num_date = float(row[2])
                is_nan_date = np.isnan(not_num_date)

            except ValueError:

                is_nan_date = False

            if is_nan_date:
                continue

            if month == self.cur_month and self.cur_day > date:
                continue

            # get the topic
            topic = row[4]

            if topic == " ":
                continue

            # get the reading pages
            pages = row[5]

            try:

                not_num_page = float(row[5])
                is_nan_page = np.isnan(not_num_page)

            except ValueError:

                is_nan_page = False

            if not is_nan_page:

                full_topic = " ".join(["HGEN 1 Class", topic, pages])

            else:
                full_topic = topic

            due_date = " ".join([str(date), str(month), str(self.cur_year)])
            print(due_date)
            item = api.items.add(full_topic,
                                 project_id=self.project_name,
                                 priority=3,
                                 due={"string": due_date}
                                 )

            api.commit()
####################################################################################################
# This is the CLI interface


def run(args):

    calendar_handler = Calendar_xlxs(args.cal, args.api)

    if args.flp:

        calendar_handler.get_all_projects()

    if args.new_task:

        calendar_handler.create_task()


def main():
    parser = argparse.ArgumentParser(
        description="This is a command line to add task to the todoist app")

    parser.add_argument("-c", "--calendar", help="This argument takes the path to the calendar excel sheet",
                        dest="cal", type=str, required=True)

    parser.add_argument("-k", "--api", help="This argument takes the users api key",
                        dest="api", type=str, required=True)

    parser.add_argument("-flp", help="This argument will print a full list of projects if set to true",
                        dest="flp", type=bool, required=False, default=False)

    parser.add_argument("-ct", "--new_task", help="This argument will create a new task",
                        dest="new_task", type=bool, required=False, default=False)

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
