from django.contrib import admin
from django.urls import path

from .views import TeammateAPIView, QuoteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/teammatelist/', TeammateAPIView.as_view()),
    path('api/v1/teammatelist/<int:pk>/', TeammateAPIView.as_view()),
    path('quotes/', QuoteAPIView.as_view(), name='quotes'),

]
