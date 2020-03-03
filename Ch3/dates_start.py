#
# Example file for working with date information
#

from datetime import date, time, datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  # today = date.today()
  # print("today's date is ", today)
  # print out the date's individual components
  # print("date components ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("today's weekday number is ", today.weekday())
  # days = ["mon", "tue", "wed", "thu", "fri", "sat"]
  # print("Which is a: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print(today)

  # Get the current time
  t = datetime.time(today)
  print(t)
  
if __name__ == "__main__":
  main();
