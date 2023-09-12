from django.urls import path
from blogs import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name ='home'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail')
    
]
