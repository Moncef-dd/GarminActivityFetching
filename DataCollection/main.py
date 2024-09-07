import os 

from session import login_to_garmin 
from save_as_csv import save_as_csv 
from fetchTest import fetch_act 

def main(): 
    userName = os.getenv("username") 
    password = os.getenv("password")

    sess = login_to_garmin(userName, password) 
    activ = fetch_act(sess)

    save_as_csv(activ)

if __name__ == '__main__': 
    main()