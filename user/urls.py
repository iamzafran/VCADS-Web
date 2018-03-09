from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='user_view'),
    url(r'^api/model/autocomplete', name='vehicle_model_auto_complete')
]