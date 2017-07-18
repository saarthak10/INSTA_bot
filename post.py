import requests
from user_id import get_user_id
from constants import *
def get_post_id(user_name):
    user_id = get_user_id(user_name)
    request_url = "{}users/{}/media/recent/?access_token={}".format(Base_url,user_id,APP_Access_Token)
    response = requests.get(request_url).json()
    if response['meta']['code'] == 200:
        if len(response['data']):

            return response['data'][0]['id']
        else:
            print("post does not exist")
    else:
        print("status code other than 200 received")


#Function for getting the number of comments on a particular post
def comments_count(user_name):
    user_id = get_user_id(user_name)
    request_url = "{}users/{}/media/recent/?access_token={}".format(Base_url, user_id, APP_Access_Token)
    response = requests.get(request_url).json()
    if response['meta']['code'] == 200:

        return response['data'][0]['comments']['count']
    else:
        print "status code not received"