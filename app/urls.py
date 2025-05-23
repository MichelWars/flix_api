from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('generos.urls')),
    path('api/v1/', include('atores.urls')),
    path('api/v1/', include('filmes.urls')),
    path('api/v1/', include('avaliacoes.urls')),
    path('api/v1/', include('authentication.urls')),
]
