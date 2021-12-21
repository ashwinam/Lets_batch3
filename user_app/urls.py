from django.urls import path, include
from .views import Register,UpdateProfile,user_change_pass


urlpatterns = [
    path('register/', Register, name='Register'),
    path('update/', UpdateProfile, name='UpdateProfile'),
    path('updatepass/', user_change_pass, name='Updatepass'),

    
   
]