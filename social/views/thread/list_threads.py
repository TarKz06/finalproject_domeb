from django.shortcuts import render
from django.db.models import Q
from django.views import View
from social.models.thread import Thread


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = Thread.objects.filter(Q(user=request.user) | Q(receiver=request.user))
        context = {
            'threads': threads
        }
        return render(request, 'social/inbox.html', context)
