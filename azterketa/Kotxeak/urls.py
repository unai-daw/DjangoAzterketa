from django.urls import path
from . import views

urlpatterns = [
    path('', views.kotxeakHTML, name='kotxeakHTML'),
    path('addCoche/', views.addCoche, name='addCoche'),
    path('addCoche/addrecord/', views.addrecord, name='addrecord'),
    path('deleteCoche/<int:id>', views.deleteCoche, name='deleteCoche'),
    path('deleteCoche/<int:id>', views.deleteCoche, name='deleteCoche'),
    path('updateCoche/<int:id>', views.updateCoche, name='updateCoche'),
    path('updateCoche/updaterecordCoche/<int:id>', views.updaterecordCoche, name='updaterecordCoche'),
    path('bistaratu/', views.bistaratu, name='bistaratu'),
    path('bistaratu2/', views.bistaratu2, name='bistaratu2'),
]
