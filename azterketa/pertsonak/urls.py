from django.urls import path
from . import views

urlpatterns = [
    path('', views.pertsonakHTML, name='pertsonakHTML'),
    path('addPer/', views.addPer, name='addPer'),
    path('addPer/addrecordPer/', views.addrecordPer, name='addrecordPer'),
    path('deletePer/<int:id>', views.deletePer, name='deletePer'),
    path('updatePer/<int:id>', views.updatePer, name='updatePer'),
    path('updatePer/updaterecordPer/<int:id>', views.updaterecordPer, name='updaterecordPer'),
]