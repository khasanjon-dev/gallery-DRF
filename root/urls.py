from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

perm = [AllowAny]
schema_view = get_schema_view(
    openapi.Info(
        title="Gallery API",
        default_version='v1',
        description="This is Gallery API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="khasanjon.eng@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=perm,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'))
]
