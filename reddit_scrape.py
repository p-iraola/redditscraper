import praw
from collections import Counter
import re

reddit_read_only = praw.Reddit(client_id ='', client_secret ='', user_agent ='')


url = ''

submission = reddit_read_only.submission(url=url)

post_comments = ''
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
	post_comments += comment.body


post_comments = post_comments.lower().split()


print(Counter(post_comments))
