import os
import csv 

from fetchTest import fetchTest 
from session import login_to_garmin

def save_as_csv(activities, filename='testDataset.csv'): 
    header = ["Activity ID", "Activity Type", "Distance", "Time"]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file) 
        # append the head 
        writer.writerow(header) 

        for activity in activities: 
            row = [
                activity["Activity ID"], 
                activity["Activity Type"], 
                activity["Distance"], 
                activity["Time"]
            ]

            writer.writerow(row)



# running the script
username = os.getenv("username")
password = os.getenv("password") 

session = login_to_garmin(username, password) 
act = fetchTest(session) 

# save to csv 
save_as_csv(act)