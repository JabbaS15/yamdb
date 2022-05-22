from django.urls import include, path
from rest_framework import routers
from users import views as user_views

from api import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'categories', views.CategoryViewSet)
router_v1.register(r'genres', views.GenreViewSet)
router_v1.register(r'titles', views.TitleViewSet)
router_v1.register(r'users', user_views.UserViewSet, basename='users')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', user_views.get_confirmation_code),
    path('v1/auth/token/', user_views.CustomTokenView.as_view()),
]
