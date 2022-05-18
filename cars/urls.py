from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name = "cars"


urlpatterns = [
    path('', views.CarListView.as_view()),
    path('add/', views.CarAddView.as_view()),
    path('<int:id>/buy/', views.CarBuyView.as_view(), name='buy'),
    # path('<int:id>/buy/', views.buy_car, name='buy'),
    path('<int:id>/available/', views.available_car, name='available'),
]
