from instagrapi import Client
import time
import random

cl = Client()

class Client:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        cl.login(username, password)
        time.sleep(random.randint(1,3))
        self.user_id = cl.user_id_from_username(username)
        time.sleep(random.randint(1,3))
    
    def get_followers(self):
        time.sleep(random.randint(1,3))
        followers_user_id = list(cl.user_followers(self.user_id).keys())
        users = []
        for user_id in followers_user_id:
            time.sleep(random.randint(5,10))
            follower_username = cl.username_from_user_id(user_id)
            users.append(follower_username)
            time.sleep(random.randint(5,10))
        return users


    def get_following(self):
        time.sleep(random.randint(1,3))
        following_user_id = list(cl.user_following(self.user_id).keys())
        users = []
        for user_id in following_user_id:
            time.sleep(random.randint(5,10))
            follower_username = cl.username_from_user_id(user_id)
            users.append(follower_username)
            time.sleep(random.randint(5,10))
        return users
    
    