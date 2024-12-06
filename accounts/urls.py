from django.urls import path
from accounts.views import signup_view,login_view,base,CustomLogout

urlpatterns = [
    path('homeview/', base, name='base'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogout, name='logout'),

]
