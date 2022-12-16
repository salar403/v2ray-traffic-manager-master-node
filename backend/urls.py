from backend import settings
from django.urls import path, re_path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

#  add the following return _static function
from django.contrib.staticfiles.views import serve


def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)


schema_view = get_schema_view(
    openapi.Info(
        title="V2ray Manager API",
        default_version="v1.0",
        description="V2ray Manager API",
        contact=openapi.Contact(email="salar40340@gmail.com"),
        license=openapi.License(name="RPS"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=settings.SWAGGER_SETTINGS["DEFAULT_API_URL"],
)

urlpatterns = [
    path("api/", include("user.urls")),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(r"^static/(?P<path>.*)$", return_static, name="static"),  #  add this line
]
