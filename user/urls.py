from django.conf.urls import url
from .views import AddUser, index


urlpatterns = [
    url(r'^$', index, name='user_view'),
    url(r'^api/adduser$', AddUser.as_view(), name='add_user_view')
]