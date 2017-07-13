import requests
from constants import APP_Access_Token,Base_url
def get_user_id(user_name):

    request_url = Base_url + 'users/search?q=%s&access_token=%s'%(user_name,APP_Access_Token)
    info = requests.get(request_url).json()

    if info['meta']['code'] == 200:
        if len(info['data']):
                return info['data'][0]['id']
        else:
            print( 'none')
    else:
        print("Status code other than 200 received")
        exit()

def get_user_info(user_name):
    user_id=get_user_id(user_name)
    response="{}/users/{}/{}".format(Base_url,user_id,APP_Access_Token)
    



