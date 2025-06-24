
from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from filmes.views import FilmesListView, NovoFilmeCreateView, FilmeDetailView, FilmeUpdateView, FilmeDeleteView
from usuarios.views import usuario_view, login_view, logout_view
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('',FilmesListView.as_view(), name='filmes_list'),
    path('users/', usuario_view, name='usuario'),
    path('admin/', admin.site.urls),
    # path('filmes/', filmes_view, name='filmes_list'),
    path('filmes/', FilmesListView.as_view(), name='filmes_list'),
    path('novo_filme/', NovoFilmeCreateView.as_view(), name='novo_filmes'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),  # pk é o id do filme
    path('filme/<int:pk>/update/', FilmeUpdateView.as_view(), name='filme_update'), 
    path('filme/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
     path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
