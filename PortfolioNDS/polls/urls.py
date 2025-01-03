from django.urls import path
from . import views

# create your urls here
app_name = 'polls'

urlpatterns = [
    path('',views.home, name='home'),
]
