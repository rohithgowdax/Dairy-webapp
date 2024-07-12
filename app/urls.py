from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path("",home,name="home"),
    path("about/",about,name="about"),
    path("contact",contact,name="contact"),
    path("accounts/", include("django.contrib.auth.urls"),name='login'),
    path("category/<slug:value>",CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>",ProductDetail.as_view(),name="product-detail"),
    path("category-title/<value>",CategoryTitle.as_view(),name="category-title"),
    #Sign Up
    path("signup/",CustomerRegistrationView.as_view(), name="signup"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)