from django.contrib import admin
from django.urls import path
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .views import Signup, Signin, ResidentListView, indexview
from django.views.generic import TemplateView
from .forms import EmailValidationOnForgotPassword
from .views import ResidentUpdateView, VehicleCreateView, VehicleDeleteView, ProfileView, VisitorListView

urlpatterns = [
    # Home page
    path("", indexview, name="index"),
    # Visitor List
    path('visitors', VisitorListView.as_view(), name='visitors_list'),
    path("signup", Signup.as_view(), name="signup"),
    path("signin", Signin.as_view(), name="signin"),
    # list of all residents
    path("list", ResidentListView.as_view(), name="users_list"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("password-reset", auth_views.PasswordResetView.as_view(template_name="password_reset.html",
         form_class=EmailValidationOnForgotPassword), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete"),
    # Update a Resident
    path('resident-update/<int:pk>',
         ResidentUpdateView.as_view(), name='resident_update'),
    # Add a vehicle
    path('vehicle-create', VehicleCreateView.as_view(), name='vehicle-create'),
    # Remove a vehicle
    path('vehicle-delete/<int:pk>',
         VehicleDeleteView.as_view(), name='vehicle-delete'),
    # Profile Page
    path('profile', ProfileView.as_view(), name='profile'),
    # Page to be redirected if the logging user is not verified yet
    path('waiting', TemplateView.as_view(
        template_name='waiting.html'), name='waiting')

]
