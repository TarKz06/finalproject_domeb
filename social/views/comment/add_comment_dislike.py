from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.comment import Comment


# The future feature doesn't have to be presented in progress 1
class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)
        user = request.user

        comment = self.dislike(comment, user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

    def dislike(self, comment, user):
        is_like = False

        for like in comment.likes.all():
            if like == user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(user)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(user)

        if is_dislike:
            comment.dislikes.remove(user)

        return comment
