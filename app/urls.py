from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, PasswordResetForm

urlpatterns = [

    path("",home,name="home"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("category/<slug:value>",CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>",ProductDetail.as_view(),name="product-detail"),
    path("category-title/<value>",CategoryTitle.as_view(),name="category-title"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("address/",ProfileView.as_view(),name="address"),


    #Sign Up
    path("signup/",CustomerRegistrationView.as_view(), name="signup"),
    #sign in
    path("login/",auth_view.LoginView.as_view(template_name="login.html",authentication_form = LoginForm) ,name='login'),  
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="password_reset.html", form_class =PasswordResetForm), name="password_reset")  

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)