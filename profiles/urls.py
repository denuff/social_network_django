from django.urls import path
from .views import my_profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view, \
    ProfileListView, send_invitation, remove_from_friends, accept_invatation, reject_invitation, \
    ProfileDetailView

app_name = 'profiles'

urlpatterns = [
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
    path('all-profiles/', ProfileListView.as_view(), name='all-profiles-view'),
    path('to-invite/', invite_profiles_list_view, name='to-invite-view'),
    path('send-invite/', send_invitation, name='send-invite'),
    path('remove-friend/', remove_from_friends, name='remove-friend'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),
    path('my-invites/acctept/', accept_invatation, name='accept-invite'),
    path('my-invites/reject/', reject_invitation, name='reject-invite'),
]
