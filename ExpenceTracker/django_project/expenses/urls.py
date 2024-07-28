from django.urls import path
from .views import IncomeCreateView, OutcomeCreateView

urlpatterns = [
    path('income/', IncomeCreateView.as_view(), name = 'add-income'),
    path('outcome/', OutcomeCreateView.as_view(), name = 'add-outcome'),
]
