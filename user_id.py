import requests
from constants import APP_Access_Token,Base_url
# function to generate user_id
def get_user_id(user_name):
#writing the url by using our base_url and app_access_token and the endpoint for user's search by name
    request_url = Base_url + 'users/search?q=%s&access_token=%s'%(user_name,APP_Access_Token)
    info = requests.get(request_url).json()

    if info['meta']['code'] == 200:
        if len(info['data']):
                return info['data'][0]['id']
        else:
            return None
    else:
        print("Status code other than 200 received")
        exit()