from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('', include('calendario.urls')),
#     path('admin/', admin.site.urls),
#     path('accounts/', include('django.contrib.auth.urls')),
# ]


urlpatterns = [
    path('', include('calendario.urls')),
    path('admin/', admin.site.urls),
    # path('api/', include('calendario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


