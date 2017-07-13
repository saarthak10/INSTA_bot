import requests
from user_id import get_user_id
from constants import *
#
def get_user_info(user_name):
    user_id = get_user_id(user_name)
    if user_id == None :
        print("No such user")
        exit()
    response = "{}users/{}/?access_token={}".format(Base_url,user_id,APP_Access_Token)
    print response
    object = requests.get(response).json()
    if object['meta']['code']==200:
        if len(object['data']):
            print(object['data']['username'])
        else:
            print('none')
    else:
        print('object code other than 200 found')

get_user_info('sharma_abhi07')






