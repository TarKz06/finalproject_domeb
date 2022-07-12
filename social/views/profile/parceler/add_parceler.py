from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile
from social.models.notification import Notification


class AddParceler(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.parcels.add(request.user)

        notification = Notification.objects.create(notification_type=8, from_user=request.user, to_user=profile.user)

        return redirect('profile', pk=profile.pk)
