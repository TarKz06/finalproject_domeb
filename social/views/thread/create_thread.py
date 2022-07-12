from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from social.models.thread import Thread
from social.forms.thread_form import ThreadForm


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        context = self.create_context(ThreadForm())
        return render(request, 'social/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')
        user = request.user
        try:
            receiver = self.get_receiver(username)
            if self.check_thread(user, receiver):
                thread = self.create_thread(user, receiver)
                return redirect('thread', pk=thread.pk)
            elif self.check_thread(receiver, user):
                thread = self.create_thread(receiver, user)
                return redirect('thread', pk=thread.pk)
            thread = self.save_thread(user, receiver, form)
            return redirect('thread', pk=thread.pk)
        except:
            messages.error(request, 'Invalid username')
            return redirect('create-thread')

    def get_receiver(self, username):
        return User.objects.get(username=username)

    def save_thread(self, user1, user2, form):
        if form.is_valid():
            thread = Thread(
                user=user1,
                receiver=user2
            )
            thread.save()
            return thread

    def check_thread(self, user1, user2):
        return Thread.objects.filter(user=user1, receiver=user2).exists()

    def create_thread(self, user1, user2):
        return Thread.objects.filter(user=user1, receiver=user2)[0]

    def create_context(self, form):
        return {
            'form': form
        }
