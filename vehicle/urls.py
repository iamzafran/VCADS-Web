from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='user_view'),
    url(r'^api/model/autocomplete/(?P<model>\D+)', views.get_vehicle_models, name='vehicle_model_auto_complete'),
    url(r'^api/adduservehicle/$', views.AddVehicleToUser.as_view(), name='add_vehicle_to_user')
]
