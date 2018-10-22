# Django viewset
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .users import views


# registriraj router
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)  # ne treba base_name jer Django rest_framework skuzi
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)
router.register('products', views.MyVehiclesViewSet, base_name='products')
router.register('category', views.MyCategoryViewSet, base_name='category')
# router.register('cart', views.MyCartViewSet, base_name='cart')



urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),

    url(r'', include(router.urls)),






]
