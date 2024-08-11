from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm
from django.contrib import admin

urlpatterns = [

    path("",home,name="home"),
    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("category/<slug:value>",CategoryView.as_view(),name="category"),
    path("product-detail/<int:pk>",ProductDetail.as_view(),name="product-detail"),
    path("category-title/<value>",CategoryTitle.as_view(),name="category-title"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("address/",adress,name="address"),
    path("updateAddress/<int:pk>",UpdateAddress.as_view(),name="updateAddress"),
    path("deleteaddress/<int:pk>",delete_address,name = 'deleteaddress'),
    path("add-to-cart/",add_to_cart,name="add_to_cart"),
    path("cart/",showcart,name="showcart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("paymentdone/",paymentdone,name='paymentdone'),
    path("orders/",orders,name='orders'),
    path("orders/",orders,name='wishlist'),
    path("search/",search,name='search'),

    path("pluscart/",pluscart),
    path("minuscart/",minuscart),
    path("removecart/",removecart),

    # path("pluswishlist/",plus_wishlist),
    # path("minuswishlist/",minus_wishlist),

    #auth
    path("signup/",CustomerRegistrationView.as_view(), name="signup"),
    path("login/",auth_view.LoginView.as_view(template_name="login.html",authentication_form = LoginForm) ,name='login'), 
    path("passwordchange/", auth_view.PasswordChangeView.as_view(template_name="passwordchange.html", form_class =
    MyPasswordChangeForm,success_url ='/passwordchangedone' ),name="passwordchange"),  
    path("passwordchangedone/", auth_view.PasswordChangeDoneView.as_view(template_name="passwordchangedone.html"),name="passwordchangedone") ,
    path('logout/', Logout, name = 'logout'),

    #password reset
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="password_reset.html", form_class =MyPasswordResetForm), name="password_reset"),
    path("password-reset/done/", auth_view.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html", form_class =MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete", auth_view.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),


    
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Neel Dairy"
admin.site.site_title = "Neel Dairy Administration"
admin.site.site_index_title = "Welcome to Neel Dairy"


