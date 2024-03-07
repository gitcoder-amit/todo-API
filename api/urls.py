from django.urls import path
from api.views import TodoView, TodoDetailView

urlpatterns = [
    path('', TodoView.as_view() ),
    path('<pk>/', TodoDetailView.as_view())
]
