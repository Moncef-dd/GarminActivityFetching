import os
#from session import login_to_garmin, username, password


def fetch_act(session): 
    activity_url = os.getenv('activityUrl')
    activityResponse = session.get(activity_url)

    data = activityResponse.json()
    # expect 2D array 
    print(data.type) 

    activities = data['activities']

    return activities; 



#session1 = login_to_garmin(username, password)
#data = fetch_act(session1); 

