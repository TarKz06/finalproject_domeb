from django.shortcuts import redirect
from django.views import View
from social.models.notification import Notification
from social.models.thread import Thread


class ThreadNotification(View):
    def get(self, request, notification_pk, object_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        thread = Thread.objects.get(pk=object_pk)
        notification = self.thread_notification(notification)
        return redirect('thread', pk=object_pk)

    def thread_notification(self, notification):
        notification.user_has_seen = True
        notification.save()
        return notification

