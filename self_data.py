import requests
from constants import APP_Access_Token,Base_url
def self_info():
    request_url=Base_url+'users/self/?access_token=%s'%(APP_Access_Token)

    user_info=requests.get(request_url).json()#json is a function pre-installed in the requests library which is used decode the response
    if user_info['meta']['code']==200:
        if len(user_info['data']):
            print ("First name:%s"%str(user_info['data']['username']))
            print("Bio:%s"%str(user_info['data']['bio']))
            print("Followers:%s"% (user_info['data']['counts']['followed_by']))
            print("Following:%s")%(user_info['data']['counts']['follows'])
            print ("Posts:%s")%(user_info['data']['counts']['media'])
        else:
            print "User does not exist"
    else:
         print("Status code not received")

self_info()

