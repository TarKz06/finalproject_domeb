from django.shortcuts import redirect
from django.views import View
from social.models.notification import Notification
from social.models.thread import Thread
from social.forms.message_form import MessageForm


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        thread = Thread.objects.get(pk=pk)
        user = request.user
        receiver = self.get_receiver(thread, user)
        message = self.create_message(thread, user, receiver, form)
        notification = self.send_notification(user, receiver, thread)
        return redirect('thread', pk=pk)

    def get_receiver(self, thread, user):
        if thread.receiver == user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        return receiver

    def create_message(self, thread, user, receiver, form):
        if form.is_valid():
            message = form.save(commit=False)
            message.thread = thread
            message.sender_user = user
            message.receiver_user = receiver
            message.save()
            return message
        return None

    def send_notification(self, user, receiver, thread):
        return Notification.objects.create(
            notification_type=4,
            from_user=user,
            to_user=receiver,
            thread=thread
        )