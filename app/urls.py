from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('add/', views.AddNewsView.as_view(), name='add_news'),
    path('edit/<int:id>/', views.NewsUpdateView.as_view(), name='edit_news'),
    path('delete/<int:id>/', views.NewsDeleteView.as_view(), name='confirm_delete'),
    path('', views.NewsMainPageView.as_view(), name='index'),
    path('add_author/', views.AddAuthorView.as_view(), name="add_author"),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('add_publisher', views.AddPublisherView.as_view(), name='add_publisher'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)