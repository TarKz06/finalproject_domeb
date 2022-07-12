from django.shortcuts import render
from django.views import View
from social.models.thread import Thread
from social.models.message import Message
from social.forms.message_form import MessageForm


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        thread = self.get_thread(pk)
        message_list = self.get_message_by_thread(pk)
        context = self.create_context(thread, MessageForm, message_list)
        return render(request, 'social/thread.html', context)

    def get_thread(self, thread_id):
        return Thread.objects.get(pk=thread_id)

    def get_message_by_thread(self, thread_id):
        return Message.objects.filter(thread__pk__contains=thread_id)

    def create_context(self, thread, form, message_list):
        return {
                'thread': thread,
                'form': form,
                'message_list': message_list
            }
