import requests
from constants import *
from post import *
def get_comments_list(username):
    media_id = get_post_id(username)
    counts = comments_count(username) #counts hold the number of comments made on the user's post
    req_url = "{}media/{}/comments?access_token={}".format(Base_url,media_id,APP_Access_Token)
    com_list = requests.get(req_url).json()
    if com_list['meta']['code'] == 200:
        if len(com_list['data']):
            numb = 0                #temporary variable numb
            while numb <counts:
                print(com_list['data'][numb]['text'])
                numb = numb + 1

        else:
            print("try again")
    else:
        print("Status code other than 200 received")

