from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Event:
    def __init__(self, name:str="", location:str="", start_date:datetime= datetime.today(), end_date:datetime=datetime.today()):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def get_name(self, value):
        self.name = value

    @property
    def get_location(self):
        return self.location

    @get_location.setter
    def get_location(self, value):
        self.location = value

    @property
    def get_start_date(self):
        return self.start_date

    @get_start_date.setter
    def get_start_date(self, value):
        format = "%Y-%m-%d"
        try:
            value = datetime.strptime(value, format)
            self.start_date = value
        except ValueError:
            raise ValueError("Format must be: YYYY-MM-DD")

    @property
    def get_end_date(self):
        return self.end_date

    @get_end_date.setter
    def get_end_date(self, value):
        format = "%Y-%m-%d"
        try:
            value = datetime.strptime(value, format)
            self.end_date = value
        except ValueError:
            raise ValueError("Format must be: YYYY-MM-DD")

    def get_duration(self):
        duration = self.end_date - self.start_date
        return duration

@dataclass
class Conference(Event):
    def __init__(self,name:str="", location:str="", start_date:datetime= datetime.today(), end_date:datetime=datetime.today(), attendees: int = 0):
        Event.__init__(self, name, location, start_date, end_date)
        self.attendees = attendees
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date


    def get_duration(self):
        duration = self.end_date - self.start_date
        return duration

def main():
    event = Event("Birthday Party", "New York", datetime(2023, 8, 25), datetime(2023, 8, 26))
    conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9, 15), datetime(2023, 9, 17), 500)

# FIX DATETIME FORMAT SO IT ONLY SHOWS DAYS/HOURS
    print("Event: ")
    print(f"Name: {event.name}")
    print(f"Location: {event.location}")
    print(f"Start date: {event.start_date}")
    print(f"End date: {event.end_date}")
    print(f"Duration (days): {event.get_duration().days}")
    print()
    print("Conference: ")
    print(f"Name: {conference.name}")
    print(f"Location: {conference.location}")
    print(f"Start date: {conference.start_date}")
    print(f"End date: {conference.end_date}")
    print(f"Attendees: {conference.attendees}")
    print(f"Duration (hours): {conference.get_duration().days * 24}")


if __name__ == "__main__":
    main()

