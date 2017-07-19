import requests
from constants import *
from user_id import get_user_id
import urllib            #library required for downloading the posts
def self_media():
    user = "{}users/self/media/recent?access_token={}".format(Base_url,APP_Access_Token)
    media=requests.get(user).json()

    if media['meta']['code'] == 200:

        if len(media['data']):



                image_name = media['data'][0]['id'] + '.jpeg'
                image_url = media['data'][0]['images']['standard_resolution']['url']
                print image_url
                urllib.urlretrieve(image_url,image_name)    #urlretrieve is used for downloading the image
                print("your recent post is downloaded")


        else:
            print('post does not exist' )
    else:
        print("status code other than 200 received ")


#Function for downloading user"s post
def user_media(user_name):


    user_id = get_user_id(user_name)

    request_url="{}users/{}/media/recent/?access_token={}".format(Base_url,user_id,APP_Access_Token)
    response=requests.get(request_url).json()

    if response['meta']['code']==200:

        if len(response['data']):
            #selecting a post according to various criteria's
            while True:
                choice = raw_input("1)To get recent post\n2)To get post with maximum likes\n3)To get maximum commented post\n4)Exit\nENTER YOUR CHOICE:")
                if choice.isdigit():
                    choice = int(choice)
                if choice == 1:
                    image_name = response['data'][0]['id'] + '.jpeg'
                    image_url = response['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url,image_name)
                    print("user's post downloaded")
                    return(response['data'][0]['id'])
                elif choice == 2:
                    number = 1
                    post_id = response['data'][0]['id']
                    while len(response['data']) > number:
                        if response['data'][number - 1]['likes']['count'] >= response['data'][number]['likes']['count']:
                                    post_id = response['data'][number - 1]['id']
                        number = number + 1

                    image_name = post_id + '.jpeg'
                    image_url = response['data'][number - 1]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    print("user's post downloaded")
                    return post_id
                elif choice ==3:
                    number = 1
                    post_id = response['data'][0]['id']
                    while len(response['data']) > number:
                        if response['data'][number - 1]['likes']['count'] >= response['data'][number]['likes']['count']:
                                    post_id = response['data'][number - 1]['id']
                        number = number + 1
                    image_name = response['data'][number - 1]['id'] + '.jpeg'
                    image_url = response['data'][number - 1]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    print("user's post downloaded")
                    return post_id
                elif choice == 4:
                    break
                else:
                    print("Select valid option\n")





            else:
                print "No post exists with less than  likes"

        else:
            print("post does not exist")
    else:
        print("status code other than 200 received")

