"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django filse
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Custom files
from Users import views as user_views
from expenses import views as expenses_views
from expenses.views import (
    IncomeDetailView,
    IncomeUpdateView,
    IncomeDeleteView,
    OutcomeDetailView,
    OutcomeUpdateView,
    OutcomeDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users app
    path('', include('Users.urls')),

    # expenses app
    path('add/', include('expenses.urls')),

        # Income
    path('income/<int:pk>/', IncomeDetailView.as_view(), name = 'income-detail'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name = 'income-update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name = 'income-delete'),
        # Outcome
    path('outcome/<int:pk>/', OutcomeDetailView.as_view(), name = 'outcome-detail'),
    path('outcome/<int:pk>/update/', OutcomeUpdateView.as_view(), name = 'outcome-update'),
    path('outcome/<int:pk>/delete/', OutcomeDeleteView.as_view(), name = 'outcome-delete'),
    
    # Logs
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Users/login.html'), name = 'login'),
    path('logout/', user_views.logout_view, name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),

    # Expenses
    path('<str:username>/income/', expenses_views.IncomeListView.as_view(), name = 'income'),
    path('<str:username>/outcome/', expenses_views.OutcomeListView.as_view(), name = 'outcome'),
    path('statistics/', expenses_views.statistics, name = 'statistics'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
