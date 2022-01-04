from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path(
        'month_with_forms/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path(
        'month_with_forms/<int:year>/<int:month>/',
        views.MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path('home/', views.HomeView.as_view(), name='home'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]