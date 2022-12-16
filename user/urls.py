from django.urls import path
from user.views import AddUser, GenerateConfig, ListUsers

urlpatterns = [
    path("user/add/", AddUser.as_view(), name="add_new_user"),
    path("user/list/", GenerateConfig.as_view(), name="list_users"),
    path("config/generate/", ListUsers.as_view(), name="create_bulk_config"),
]