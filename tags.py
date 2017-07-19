import requests
from constants import *       #importing Base_url and App_Access_token
import matplotlib.pyplot as plt  #importing the library matplotlib for plotting the graph

def analysing_trends():
    media_count = []         #list for keeping the media_counts of different tags
    list_of_tags = []   #list for keeping the list of tags
#getting user input for the tags he wants to know about
    for i in range(0,5):
        text = raw_input("Enter the name for the caption you need the data ")
        list_of_tags.append(text)

#using get request to get the response
    for j in range(len(list_of_tags)):

        requests_url = "{}tags/{}?access_token={}".format(Base_url, list_of_tags[j], APP_Access_Token)#using the endpoint for searching for a tag
        response = requests.get(requests_url).json()  #response is the json()  object which keeps the data decoded by json()
        if response['meta']['code'] == 200:
            if len(response['data']) :
                media_count.append(response['data']['media_count'])

            else:

                media_count.append(0)


        else:
            print(response)
            print("Status code other than 200 received")
    #To analyse most popular tag
    for n in range(len(media_count)-1):


        if media_count[n] >= media_count[n+1]: #checking if the first element is greater or not
           swap = media_count[n+1]   #swapping with the next number in the list

           media_count[n+1] = media_count[n]#at the end of this loop the largest element in the list will be at the end of the list count
           media_count[n] = swap

           temp = list_of_tags[n+1]#temporary variable temp for swapping of corresponding tag in list_of_tags
           list_of_tags[n+1] =list_of_tags[n]
           list_of_tags[n] = temp
        else:
            media_count[n+1] = media_count[n+1]
    n = len(media_count)-1
    print"Most popular tag is:%s"%(list_of_tags[n])


    #plotting the graph between the tags and no of posts  using matplotlib

    left = [1,2,3,4,5]
    height = media_count
    tick_label = ['one','two','three','four','five']
    plt.bar(left,height,tick_label = tick_label,width = 0.5,color=['blue','green'])
    plt.ylabel("no of posts")
    plt.xlabel("Tags")
    plt.show()


