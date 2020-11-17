from instapy import InstaPy

# Open browser and login automatically to Instagram account
session = InstaPy(username="your_username", password="your_password").login()

session.login()

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

#Don't follow accout with over 8500 followers
session.set_relationship_bounds(enabled=True, max_followers=8500)

# Using Clarifai API to filter out NSFW posts
session.set_use_clarifai(enabled=True, api_key='your_api_key')
session.clarifai_check_img_for(['nsfw'])

# Posts to like search by listed tags
session.like_by_tags(["python","javascript", "websitedesigner", "computerengineering"], amount=1)

# posts to avoid by tag and content
session.set_dont_like(["naked", "nsfw", "snake", "breed", "reptiles"])

# Follow 50% of users that post the liked content
session.set_do_follow(True, percentage=50)

# leave comment on 50% of the post
session.set_do_comment(True, percentage=100)
#Comments to leave on posts
session.set_comments(["Nice!", "cool!", "Beautiful :heart_eyes:"])

#End session and logout
session.end()