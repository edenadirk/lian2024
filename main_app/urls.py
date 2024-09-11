
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Static pages
    path('', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('donorInfo/', views.donorInfo, name='donorInfo'),
    path('recipientInfo/', views.recipientInfo, name='recipientInfo'),

    # Profiles
    path('profile/index/', views.profileIndex, name='profileIndex'),
    path('profile/addProfile/', views.addProfile, name='addProfile'),
    path('profile/<int:user_id>/', views.showProfile, name='showProfile'),
    path('profile/myProfile/', views.myProfile, name='myProfile'),
    path('profile/<int:user_id>/edit', views.editProfile, name='editProfile'),
    path('profile/<int:user_id>/delete/', views.deleteProfile, name='deleteProfile'),

    # Posts
    path('post/add/', views.addPost, name='addPost'),
    path('post/<int:post_id>/', views.showPost, name='showPost'),
    path('post/<int:post_id>/edit', views.editPost, name='editPost'),
    path('post/<int:post_id>/delete/', views.deletePost, name='deletePost'),

    # Search
    path('search/', views.search_view, name='search'),

    # Authentication
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/signup/', views.signup, name='signup'),

    # Analytics
    path('powerbi-report/', views.redirect_to_powerbi, name='powerbi_report'),
    path('analytics/', views.analytics_redirect, name='analytics'),

    # Notifications
    path('get-notification-count/', views.get_notification_count, name='get_notification_count'),
    path('notifications/', views.notifications_list, name='notifications_list'),

    #Donations handle views
    path('add-donation-request/<int:post_id>/', views.add_donation_request, name='addDonationRequest'),
    path('handle-donation-action/', views.handle_donation_action, name='handle_donation_action'),
    path('mark-notification-as-read/', views.mark_notification_as_read, name='mark_notification_as_read'),]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
