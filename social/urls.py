from django.urls import path
from social.views.post.post_list import PostListView
from social.views.post.post_detail import PostDetailView, PostEditView, PostDeleteView, CommentDeleteView, ProfileView, ProfileEditView, AddFollower, RemoveFollower, AddLike, AddDislike, UserSearch, ListFollowers, AddCommentLike, AddCommentDislike, CommentReplyView, PostNotification, FollowNotification, ThreadNotification, RemoveNotification, CreateThread, ListThreads, ThreadView, CreateMessage, AddNoiser, RemoveNoiser, AddServicer, RemoveServicer, NoiseNotification, ServiceNotification, AddRepairer, RemoveRepairer, RepairNotification, AddParceler, RemoveParceler, ParcelNotification, ListNoisers, ListServicers, ListRepairers, Listparcelers

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
