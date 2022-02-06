from django.urls import path
from .api.viewsets import Create, List, Detail, Update, Delete
app_name = 'blog_api'

urlpatterns = [
    path('list/', List.as_view(), name='list'),
    path('create/', Create.as_view(), name='create'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]