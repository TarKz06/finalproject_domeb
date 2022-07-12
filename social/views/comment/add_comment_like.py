from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.comment import Comment
from social.models.notification import Notification


# The future feature doesn't have to be presented in progress 1
class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        user = request.user
        comment = self.like(comment, user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    def like(self, comment, user):
        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(user)

        is_like = False

        for like in comment.likes.all():
            if like == user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(user)
            notification = self.create_notification(comment, user)

        if is_like:
            comment.likes.remove(user)

        return comment

    def create_notification(self, comment, user):
        return Notification.objects.create(notification_type=1, from_user=user,
                                           to_user=comment.author, comment=comment)
