from django.urls import path
from mytodo import views

urlpatterns = {
    # path('addTask',views.addTask,name = 'addTask'),
    path('',views.home,name='home'),
    path('done/<int:pk>',views.mark_done1,name='markDone'),
    path('undone/<int:pk>',views.mark_undone1,name='markUndone'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
    path('addTask',views.addTask,name='addTask')
}