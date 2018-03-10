from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.index, name='user_view'),
    url(r'^api/model/autocomplete/(?P<model>\D+)', views.get_vehicle_models, name='vehicle_model_auto_complete'),
    url(r'^api/adduservehicle/$', views.AddVehicleToUser.as_view(), name='add_vehicle_to_user'),
    url(r'^api/getuservehicle/(?P<uuid>[a-zA-Z0-9]+)', views.get_user_vehicle, name='get_user_vehicle'),

]
