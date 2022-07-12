from django.shortcuts import render, redirect
from django.views import View
from social.models.post import Post
from social.models.user_profile import UserProfile


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')

        followers = profile.followers.all()
        noisers = profile.noises.all()
        servicers = profile.services.all()
        repairers = profile.repairs.all()
        parcelers = profile.parcels.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        # ======================================================

        if len(noisers) == 0:
            is_noising = False

        for noiser in noisers:
            if noiser == request.user:
                is_noising = True
                break
            else:
                is_noising = False

        # ======================================================

        if len(servicers) == 0:
            is_servicing = False

        for servicer in servicers:
            if servicer == request.user:
                is_servicing = True
                break
            else:
                is_servicing = False

        # ======================================================

        if len(repairers) == 0:
            is_repairing = False

        for repairer in repairers:
            if repairer == request.user:
                is_repairing = True
                break
            else:
                is_repairing = False

        # ======================================================

        if len(parcelers) == 0:
            is_parceling = False

        for parceler in parcelers:
            if parceler == request.user:
                is_parceling = True
                break
            else:
                is_parceling = False

        number_of_followers = len(followers)
        number_of_noisers = len(noisers)
        number_of_servicers = len(servicers)
        number_of_repairers = len(repairers)
        number_of_parcelers = len(parcelers)

        context = {
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

        return render(request, 'social/profile.html', context)
