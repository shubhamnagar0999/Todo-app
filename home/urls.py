from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('task',views.task,name="task"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
]
