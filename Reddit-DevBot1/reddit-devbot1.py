import praw
from requests import Session

session = Session()
reddit = praw.Reddit(client_id='wRFNcU35MOVrdw',
                     client_secret='wemY5QhP5i_tO3alR19HPHRoRRY',
                     user_agent='testscript by /u/rohith_v',
                     username='rohith_v',
                     password='spijuiw97')

print(reddit.user.me())
print(reddit.auth.scopes())

for post in reddit.subreddit('showerthoughts').new(limit=25):
    print(post.title)