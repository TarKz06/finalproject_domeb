from django.contrib import admin
from social.models.post import Post
from social.models.comment import Comment
from social.models.user_profile import UserProfile
from social.models.notification import Notification
from social.models.images import Image
from social.models.message import Message
from social.models.thread import Thread

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Thread)
admin.site.register(Image)
admin.site.register(Message)
