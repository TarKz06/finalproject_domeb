from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


# List issue
class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        followers = self.get_all_follower(pk)
        context = self.create_context(self.get_profile(pk), followers)
        return render(request, 'social/followers_list.html', context)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def get_all_follower(self, user_id):
        profile = self.get_profile(user_id)
        return profile.followers.all()

    def create_context(self, profile, followers):
        return {
            'profile': profile,
            'followers': followers,
        }
