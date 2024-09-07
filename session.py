import requests
from bs4 import BeautifulSoup 
import os

def login_to_garmin(username, password):
    loginUrl = "https://connect.garmin.com/signin"
    session = requests.Session()

    response = session.get(loginUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    csrf_token = soup.find('input', {'name': 'csrfToken'})['value']

    login_data = {
        'username' : username, 
        'password' : password, 
        'csrfToken' : csrf_token 
    } 

    session.post(loginUrl, data=login_data)

    return session 


#username = os.getenv("username")
#password = os.getenv("password")