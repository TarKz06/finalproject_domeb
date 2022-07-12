from django.http import HttpResponse
from django.views import View
from social.models.notification import Notification


class RemoveNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)

        notification = self.delete_notification(notification)

        return HttpResponse('Success', content_type='text/plain')

    def delete_notification(self, notification):
        notification.user_has_seen = True
        notification.save()
        return notification
