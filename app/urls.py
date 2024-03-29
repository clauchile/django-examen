from django.urls import path
from . import views, auth
urlpatterns = [
    path('', views.index),
    path('registro/', auth.registro),
    path('login/', auth.login),
    path('logout/', auth.logout),
     path('editar/<int:dato>/', auth.editar),
    # path('muro/', views.muro, name = 'muro'),
    path('muro/', views.muro),
    path('cita/', views.muro),

    path('muro/<int:val>/', views.like),
    path('muro/ajax/<int:val>/', views.like_ajax),

    path('muro/<int:num>/delete', views.cita_delete),
    path('muro/ajax/delete/<int:num>/', views.cita_delete_ajax),

    path('user/<int:num>/', views.cita_usuario)
    # path('muro/<int:num>/mensaje/delete', views.mensaje_delete),
    
]
