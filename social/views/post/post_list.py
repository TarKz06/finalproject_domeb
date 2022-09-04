from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.images import Image
from social.forms.post_form import PostForm
from social.models.post import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from social.serializers import PostSerializer
from linebot import LineBotApi
from linebot.models import TextSendMessage


class PostListView(LoginRequiredMixin, View, ):

    def get(self, request, *args, **kwargs):
        posts = self.post_list(request.user)
        context = self.create_context(posts, PostForm())

        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = self.post_list(request.user)
        form = PostForm(request.POST, request.FILES)
        files = request.FILES.getlist('image')
        new_post = self.create_post(form, request.user,files)
        context = self.create_context(posts,form)

        line_bot_api = LineBotApi('g0DnCQ6ow5PB5z4md9trhxi+rJZ56WL/K78bkvLC0lR9b1/jy/QfhSdghiqB43bzPI/KehWMnZSuCIwH7ZBc0yVO5rohSqXFv875qo/aLDZ9RFakOxofQiRkfbgsQbHQWwx04O/CHBIe/TP0Y8MckQdB04t89/1O/w1cDnyilFU=')
        line_bot_api.multicast(['U285313a7c811bb8d6805fe56c97951f2', 'U5d40816d9cc998f21dec8bb56b54b18d'], TextSendMessage(text='Notification!!  You have a new announcement in Domeb web application.'))

        print('post created !!!')
        return render(request, 'social/post_list.html', context)

    def create_post(self, form, user, files):
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = user
            new_post.save()

            for f in files:
                img = Image(image=f)
                img.save()
                new_post.image.add(img)

            return new_post.save()
        return None

    def post_list(self, user):
        return Post.objects.filter(
            author__profile__followers__in=[user.id]
        ).order_by('-created_on')

    def create_context(self, post, form):
        return {
            'post_list': post,
            'form': form,
        }

@api_view()
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
