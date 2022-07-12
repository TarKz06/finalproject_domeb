from django.shortcuts import redirect
from django.views import View
from social.models.post import Post
from social.models.notification import Notification


class PostNotification(View):
    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        post = Post.objects.get(pk=post_pk)

        notification = self.delete_notification(notification)

        return redirect('post-detail', pk=post_pk)

    def delete_notification(self, notification):
        notification.user_has_seen = True
        notification.save()
        return notification
