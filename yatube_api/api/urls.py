from rest_framework import routers

from django.urls import include, path

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_version_1 = routers.DefaultRouter()
router_version_1.register('posts', PostViewSet, basename='posts')
router_version_1.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router_version_1.register('groups', GroupViewSet, basename='groups')
router_version_1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_version_1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
