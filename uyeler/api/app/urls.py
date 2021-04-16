from django.urls import path
from api.app import views as api_views

urlpatterns = [
    
    path('users/',api_views.UserListCreateView.as_view(), name='users-listesi' ),
    path('users/<int:pk>', api_views.UserDetailAPIView.as_view(), name ='user-detay'),
    
]

#FUNCTION BASED VIEWS
# urlpatterns = [
    
#     path('users/', api_views.user_list_create_api_view, name='users-listesi' ),
#     path('users/<int:pk>', api_views.user_detail_api_view, name ='user-detay'),
    
# ]