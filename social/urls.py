from django.urls import path

# post sub feature
from social.views.post.post_list import PostListView
from social.views.post.post_detail import PostDetailView
from social.views.post.post_edit import PostEditView
from social.views.post.post_delete import PostDeleteView
from social.views.post.add_dislike import AddDislike
from social.views.post.add_like import AddLike
from social.views.post.post_notification import PostNotification

# comment sub feature
from social.views.comment.comment_delete import CommentDeleteView
from social.views.comment.add_comment_like import AddCommentLike
from social.views.comment.add_comment_dislike import AddCommentDislike
from social.views.comment.comment_reply import CommentReplyView

# thread sub feature
from social.views.thread.thread_notification import ThreadNotification
from social.views.thread.create_thread import CreateThread
from social.views.thread.list_threads import ListThreads
from social.views.thread.create_message import CreateMessage
from social.views.thread.thread import ThreadView

# profile sub feature
from social.views.profile.profile import ProfileView
from social.views.profile.profile_edit import ProfileEditView
from social.views.profile.user_search import UserSearch

# follower sub feature
from social.views.profile.follower.add_follower import AddFollower
from social.views.profile.follower.remove_follower import RemoveFollower
from social.views.profile.follower.list_followers import ListFollowers
from social.views.profile.follower.follow_notification import FollowNotification

# noiser sub feature
from social.views.profile.noiser.add_noiser import AddNoiser
from social.views.profile.noiser.remove_noiser import RemoveNoiser
from social.views.profile.noiser.noise_notification import NoiseNotification
from social.views.profile.noiser.list_noisers import ListNoisers

# servicer sub feature
from social.views.profile.servicer.add_servicer import AddServicer
from social.views.profile.servicer.remove_servicer import RemoveServicer
from social.views.profile.servicer.service_notification import ServiceNotification
from social.views.profile.servicer.list_servicers import ListServicers

# repairer sub feature
from social.views.profile.repairer.add_repairer import AddRepairer
from social.views.profile.repairer.remove_repairer import RemoveRepairer
from social.views.profile.repairer.repair_notification import RepairNotification
from social.views.profile.repairer.list_repairers import ListRepairers

# parceler sub feature
from social.views.profile.parceler.add_parceler import AddParceler
from social.views.profile.parceler.remove_parceler import RemoveParceler
from social.views.profile.parceler.parcel_notification import ParcelNotification
from social.views.profile.parceler.list_parcelers import Listparcelers

# notification sub feature
from social.views.notification.remove_notification import RemoveNotification

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name='comment-reply'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),

    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/noisers/', ListNoisers.as_view(), name='list-noisers'),
    path('profile/<int:pk>/servicers/', ListServicers.as_view(), name='list-servicers'),
    path('profile/<int:pk>/repairers/', ListRepairers.as_view(), name='list-repairers'),
    path('profile/<int:pk>/parcelers/', Listparcelers.as_view(), name='list-parcelers'),

    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('profile/<int:pk>/noisers/add', AddNoiser.as_view(), name='add-noiser'),
    path('profile/<int:pk>/noisers/remove', RemoveNoiser.as_view(), name='remove-noiser'),
    path('profile/<int:pk>/services/add', AddServicer.as_view(), name='add-servicer'),
    path('profile/<int:pk>/services/remove', RemoveServicer.as_view(), name='remove-servicer'),
    path('profile/<int:pk>/repairs/add', AddRepairer.as_view(), name='add-repairer'),
    path('profile/<int:pk>/repairs/remove', RemoveRepairer.as_view(), name='remove-repairer'),
    path('profile/<int:pk>/parcels/add', AddParceler.as_view(), name='add-parceler'),
    path('profile/<int:pk>/parcels/remove', RemoveParceler.as_view(), name='remove-parceler'),

    path('search/', UserSearch.as_view(), name='profile-search'),
    path('notification/<int:notification_pk>/post/<int:post_pk>', PostNotification.as_view(), name='post-notification'),

    path('notification/<int:notification_pk>/profile/<int:profile_pk>', FollowNotification.as_view(), name='follow-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', NoiseNotification.as_view(), name='noise-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', ServiceNotification.as_view(), name='service-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', RepairNotification.as_view(), name='repair-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>', ParcelNotification.as_view(), name='parcel-notification'),

    path('notification/<int:notification_pk>/thread/<int:object_pk>', ThreadNotification.as_view(), name='thread-notification'),
    path('notification/delete/<int:notification_pk>', RemoveNotification.as_view(), name='notification-delete'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
]
