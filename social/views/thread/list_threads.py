from django.shortcuts import render
from django.db.models import Q
from django.views import View
from social.models.thread import Thread


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        context = self.create_context(Thread.objects.filter(Q(user=request.user) | Q(receiver=request.user)))
        return render(request, 'social/inbox.html', context)

    def create_context(self, threads):
        return {
            'threads': threads
        }
