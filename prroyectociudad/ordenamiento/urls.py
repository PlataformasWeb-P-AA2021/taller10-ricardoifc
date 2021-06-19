from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('to_list/parroquia', views.to_list_parroquia, 
            name='to_list_parroquia'),
        path('to_list/barrio', views.to_list_barrio, 
            name='to_list_barrio'),        
        path('add/parroquia', views.add_parroquia,
            name='add_parroquia'),
        path('add/barrio', views.add_barrio,
            name='add_barrio'),
        path('edit/parroquia/<int:id>', views.edit_parroquia, 
            name='edit_parroquia'),
        path('edit/barrio/<int:id>', views.edit_barrio, 
            name='edit_barrio'),
 ]