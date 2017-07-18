from user_id import get_user_id
from user_info import get_user_info
from self_data import self_info
from media import *
from post import *
from comment_list import get_comments_list
from like import like_post
from tags import analysing_trends
from comments import post_comment



def insta_bot():

    Name= raw_input("Enter your instabot username")
    print("WELCOME TO INSTABOT!!!\n")
    print("Hello %s\n")%(Name)
    print("What would you like to do?\n")
    while True:
        choose = raw_input("1)Get own information\n2)Get user id\n3)Get user's information\n4)Get your own recent post\n5)Get user's recent post\n6)Post a like on a user's post\n"
                       "7)Comment on a user's post\n8)Get a list of comments on a user's post\n9)Analyse popular trends\n10)Exit")
        if choose.isdigit():
            choose = int(choose)
        if choose == 1:
            self_info()
        elif choose == 2:
            Username = raw_input("Enter username of the user whose id is required")
            get_user_id(Username)
        elif choose == 3:
            user_name = "Enter the username of the user whose details are required"
            get_user_info()
        elif choose == 4:
            self_media()
        elif choose == 5:
            user_media()
        elif choose == 6:
            user_name = raw_input("Enter the username of the user")
            like_post(user_name)
        elif choose == 7:
            user_name = ("Enter the username of the user ")
            post_comment(user_name)
        elif choose == 8:
            analysing_trends()
        elif choose == 9:
            user_name = raw_input("Enter the username of the user")
        elif choose == 10:
            break
        else:
            ("Enter valid option\n")

insta_bot()