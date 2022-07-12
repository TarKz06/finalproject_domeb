from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.post import Post
from social.models.comment import Comment
from social.models.notification import Notification
from social.forms.comment_form import CommentForm


# The future feature doesn't have to be presented in progress 1
class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        new_comment = self.reply(parent_comment, post, form, request.user)

        notification = Notification.objects.create(notification_type=2, from_user=request.user,
                                                   to_user=parent_comment.author, comment=new_comment)

        return redirect('post-detail', pk=post_pk)

    def reply(self, comment, post, form, user):
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.post = post
            new_comment.parent = comment
            new_comment.save()
        return comment
