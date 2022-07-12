from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.post import Post
from social.models.notification import Notification


# The future feature doesn't have to be presented in progress 1
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        user = request.user
        post = self.like(post, user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    def like(self, post, user):
        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(user)

        is_like = False

        for like in post.likes.all():
            if like == user:
                is_like = True
                break

        if not is_like:
            post.likes.add(user)
            notification = self.create_notification(post, user)
        if is_like:
            post.likes.remove(user)

        return post

    def create_notification(self, post, user):
        return Notification.objects.create(notification_type=1, from_user=user, to_user=post.author,
                                           post=post)
