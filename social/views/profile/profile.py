from django.shortcuts import render, redirect
from django.views import View
from social.models.post import Post
from social.models.user_profile import UserProfile


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = self.get_profile(pk, request.user)
        context = self.create_context(
            profile.get('user'),
            profile.get('profile'),
            profile.get('posts'),
            profile.get('number_of_followers'),
            profile.get('is_following'),
            profile.get('number_of_noisers'),
            profile.get('is_noising'),
            profile.get('number_of_servicers'),
            profile.get('is_servicing'),
            profile.get('number_of_repairers'),
            profile.get('is_repairing'),
            profile.get('number_of_parcelers'),
            profile.get('is_parceling'),
        )
        return render(request, 'social/profile.html', context)

    def create_context(
            self,
            user,
            profile,
            posts,
            number_of_followers,
            is_following,
            number_of_noisers,
            is_noising,
            number_of_servicers,
            is_servicing,
            number_of_repairers,
            is_repairing,
            number_of_parcelers,
            is_parceling
    ):
        return {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'number_of_noisers': number_of_noisers,
            'is_noising': is_noising,
            'number_of_servicers': number_of_servicers,
            'is_servicing': is_servicing,
            'number_of_repairers': number_of_repairers,
            'is_repairing': is_repairing,
            'number_of_parcelers': number_of_parcelers,
            'is_parceling': is_parceling,
        }

    def check_following(self, followers,user):
        if len(followers) == 0:
            return False
        for follower in followers:
            if follower == user:
                return True
        return False

    def check_noiser(self, noisers, user):
        if len(noisers) == 0:
            return False

        for noiser in noisers:
            if noiser == user:
                return True
        return False

    def check_servicer(self, servicers, user):
        if len(servicers) == 0:
            return False

        for servicer in servicers:
            if servicer == user:
                return True
        return False

    def check_repariers(self, repairers, user):
        if len(repairers) == 0:
            return False

        for repairer in repairers:
            if repairer == user:
                return True
        return False

    def check_parcelers(self, parcelers, user):
        if len(parcelers) == 0:
            return False

        for parceler in parcelers:
            if parceler == user:
                return True
        return False

    def get_profile(self, user_id, current_user):
        profile = UserProfile.objects.get(pk=user_id)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        followers = profile.followers.all()
        noisers = profile.noises.all()
        servicers = profile.services.all()
        repairers = profile.repairs.all()
        parcelers = profile.parcels.all()
        is_following = self.check_following(followers, current_user)
        is_noising = self.check_noiser(noisers, current_user)
        is_servicing = self.check_servicer(servicers, current_user)
        is_repairing = self.check_repariers(repairers, current_user)
        is_parceling = self.check_parcelers(parcelers, current_user)

        number_of_followers = len(followers)
        number_of_noisers = len(noisers)
        number_of_servicers = len(servicers)
        number_of_repairers = len(repairers)
        number_of_parcelers = len(parcelers)

        return {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'number_of_noisers': number_of_noisers,
            'is_noising': is_noising,
            'number_of_servicers': number_of_servicers,
            'is_servicing': is_servicing,
            'number_of_repairers': number_of_repairers,
            'is_repairing': is_repairing,
            'number_of_parcelers': number_of_parcelers,
            'is_parceling': is_parceling,
        }
