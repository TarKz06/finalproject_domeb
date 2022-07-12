from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.post import Post


# The future feature doesn't have to be presented in progress 1
class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        user = request.user
        post = self.dislike(post,user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    def dislike(self, post, user):
        is_like = False

        for like in post.likes.all():
            if like == user:
                is_like = True
                break

        if is_like:
            post.likes.remove(user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(user)

        if is_dislike:
            post.dislikes.remove(user)

        return post
