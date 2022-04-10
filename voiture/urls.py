from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('product', views.viewsettotalproduct, basename="products")
router.register('voiture', views.viewsetCarsProduct, basename="cars")
urlpatterns=[
	path('', include(router.urls)),
	path('obtainToken/', obtain_auth_token),
	path("user/", views.Generateuser.as_view()),

] 