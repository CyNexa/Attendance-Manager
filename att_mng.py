# Imports
import pandas as pd
from datetime import datetime
import os

# Data Storing
dataFile = 'attendance.csv'

if os.path.exists(dataFile):
    attendData = pd.read_csv(dataFile)
else: 
    attendData = pd.DataFrame(columns=['Date', 'Day', 'Scheduled', 'Attended'])

# Function Stating
currDnT = datetime.now()
today = currDnT.strftime('%A')

todayDate = datetime.now().strftime('%d-%m-%Y')

# Defines
def dailyWish():
    if today == "Sunday" or today == "Monday":
        print("Its Holiday, Enjoy!")
        return 0
    elif today == "Tuesday":
        print("Its Tuesday, 6 Class Today!")
        return 6
    elif today == "Wednesday":
        print("Its Wednesday, 6 Class Today!")
        return 6
    elif today == "Thursday":
        print("Its Thursday, 4 Class Today!")
        return 4
    elif today == "Friday":
        print("Its Friday, 6 Class Today!")
        return 6
    elif today == "Saturday":
        print("Its Saturday, 5 Class Today!")
        return 5

def attendances(day, scheduled, attended):
    global attendData
    dailyData = pd.DataFrame({
        'Date': [todayDate],
        'Day': [day],
        'Scheduled': [scheduled],
        'Attended': [attended]})
    attendData = pd.concat([attendData, dailyData], ignore_index=True)

# Base Code Here
if __name__ == "__main__":
    today_day = datetime.now().strftime('%A')
    schedClass = dailyWish()
    if schedClass > 0:
        attended_classes = int(input(f"How many classes did you attend today? "))
        attendances(today_day, schedClass, attended_classes)
    
    # Display the updated data
    print("\nAttendance Spreadsheet:")
    print(attendData)
    
    # Save the updated DataFrame to CSV
    attendData.to_csv(dataFile, index=False)