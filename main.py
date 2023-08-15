from instagrapi import Client

username = "" # enter username
password = "" # enter password

user = Client(username, password)
print(user.username)