from django.urls import path
from .views import form, list1, Edit_Data,Delete_Data,viewme

urlpatterns = [
    path('', form, name='form'),
    path('list1/', list1, name='list1'),
    path('Edit_Data/<str:full_name>/', Edit_Data, name='edit_data'),
    path('Delete_Data/<str:full_name>/', Delete_Data, name='delete_data'), 
    path('viewme/<str:full_name>/', viewme, name='viewme'),  
]
