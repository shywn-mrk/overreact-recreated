from rest_framework.routers import DefaultRouter

from blog.api.viewsets import PostViewSet

router = DefaultRouter()

router.register('posts', viewset=PostViewSet, basename='posts')
