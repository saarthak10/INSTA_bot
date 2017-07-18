import requests
from user_id import get_user_id
from constants import *
#get user info using the user_id
user_name = raw_input("enter the name of the user")
def get_user_info(user_name):
    #first we need to know the id of the user which is generated by using the get_user_id function
    user_id = get_user_id(user_name)
    if user_id == None :
        print("No such user")
        exit()
    response = "{}users/{}/?access_token={}".format(Base_url,user_id,APP_Access_Token)
    object = requests.get(response).json()
    if object['meta']['code']==200:
        if len(object['data']):
            print("Name:%s")%(object['data']['username'])
            print("Followers:%s")%(object['data']['counts']['followed_by'])
            print("Following:%s")%(object['data']['counts']['follows'])
        else:
            print('none')
    else:
        print('status code other than 200 found')

get_user_info(user_name)






