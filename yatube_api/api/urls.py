from rest_framework import routers

from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router_version_1 = routers.DefaultRouter()
router_version_1.register('posts', PostViewSet, basename='posts')
router_version_1.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router_version_1.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router_version_1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt'))
]
