# Project 4: Simple Alarm clock
# Description: This program ask the user to enter the time (HH:MM format).
# Its keep checking the system time every minute and alerts when it matches the time.

import datetime
import time

#Ask user to enter alarm time
alarm_time = input("Enter the time for the alarm in 'HH:MM' format: ")

#split the alarm thime into hours and minutes
alarm_hour , alarm_minute = map(int, alarm_time.split(":"))

print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")

#Infinite loop to check time
while True:
    now = datetime.datetime.now() # get current time
    current_hour,current_minute = now.hour, now.minute

    #Compare current time with alarm time
    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("Time to wake up!!")
        break

    #wait for 60 seconds before checking again
    time.sleep(60)