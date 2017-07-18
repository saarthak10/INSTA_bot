import requests
from constants import *
from post import get_post_id
def post_comment(user_name):
    media_id = get_post_id(user_name)
    comment_text = raw_input("enter your comment:")
    req_url = "{}media/{}/comments".format(Base_url,media_id)
    payload = {"access_token":APP_Access_Token, "text":comment_text}
    print("post request url:%s")%(req_url)
    comment = requests.post(req_url,payload).json()
    if comment['meta']['code'] == 200:
        print("Your comment is added")
    else:
        print("Unable to post comment,try again")
post_comment('sharma_abhi07')



