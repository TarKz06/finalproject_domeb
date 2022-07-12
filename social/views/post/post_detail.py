from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.post import Post
from social.models.comment import Comment
from social.models.notification import Notification
from social.forms.comment_form import CommentForm


class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = self.details(pk)
        comments = self.comment_details(post)
        form = CommentForm()
        context = self.create_context(post, form, comments)

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = self.details(pk)
        form = CommentForm(request.POST)
        notification = self.create_notification(request.user, post)
        comments = self.create_comment(post, form, request.user)
        context = self.create_context(post, form, comments)

        return render(request, 'social/post_detail.html', context)

    def create_notification(self, user, post):
        return Notification.objects.create(notification_type=2, from_user=user, to_user=post.author,
                                           post=post)

    def create_comment(self, post, form, user):
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')
        return comments

    def details(self, id):
        return Post.objects.get(pk=id)

    def comment_details(self, post):
        return Comment.objects.filter(post=post).order_by('-created_on')

    def create_context(self, post, form, comments):
        return {
            'post': post,
            'form': form,
            'comments': comments,
        }
