from django.contrib import admin
from social.model.post import Post
from social.model.comment import Comment
from social.model.user_profile import UserProfile
from social.model.notification import Notification
from social.model.images import Image
from social.model.message import Message
from social.model.thread import Thread

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Thread)
admin.site.register(Image)
admin.site.register(Message)
