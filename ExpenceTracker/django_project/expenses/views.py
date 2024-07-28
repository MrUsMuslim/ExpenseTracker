# Types
from typing import Any, List
from django.http import HttpResponse
from django.forms import BaseModelForm
from django.db.models.query import QuerySet

# Django files
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


# Custom files
from .models import Income, Outcome
from Backend.main import (
    get_total,
    get_percentage,
    get_total_last_7_days,
    get_total_last_30_days,
    get_total_last_365_days
)


# INCOME VIEWS
class IncomeCreateView(LoginRequiredMixin, CreateView):
    """
    Income create View\n
    name => add-income
    """

    model = Income
    fields: list[str] = ['typeof', 'date', 'amount', 'description']

    template_name: str = 'expenses/add_income.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class IncomeListView(LoginRequiredMixin, ListView):
    """
    Income List View\n
    name => income
    """

    # Settings
    model = Income
    template_name: str = 'expenses/income.html'
    context_object_name: str = 'database_income'
    paginate_by: int = 4

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Income.objects.filter(owner = user).order_by('-date')


class IncomeDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    """
    Income Detail View\n
    name => income-detail
    """

    model = Income

    def test_func(self) -> bool:
        income: Income = self.get_object()
        return  self.request.user == income.owner


class IncomeUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    Income Upadate View\n
    name => income-update
    """

    model = Income
    fields: list[str] = ['typeof', 'date', 'amount', 'description']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        income: Income = self.get_object()
        return  self.request.user == income.owner


class IncomeDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    Income Delete View\n
    name => income-delete
    """

    model = Income
    success_url: str = "/"

    def test_func(self) -> bool:
        income: Income = self.get_object()
        return  self.request.user == income.owner



# OUTCOME VIEWS
class OutcomeCreateView(LoginRequiredMixin, CreateView):
    """
    Outcome Create View\n
    name => add-outcome
    """

    model = Outcome
    fields: list[str] = ['typeof', 'date', 'amount', 'description']

    template_name: str = 'expenses/add_outcome.html'
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OutcomeListView(LoginRequiredMixin, ListView):
    """
    Outcome List View\n
    name => outcome
    """

    # Settings
    model = Outcome
    template_name: str = 'expenses/outcome_list.html'
    context_object_name: str = 'database_outcome'
    ordering: list[str] = ['-date']

    paginate_by: int = 4


class OutcomeDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    """
    Outcome Detail View\n
    name => outcome-detail
    """

    model = Outcome

    def test_func(self) -> bool:
        outcome: Outcome = self.get_object()
        return  self.request.user == outcome.owner


class OutcomeUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    Outcome Update View\n
    name => outcome-update
    """

    model = Outcome
    fields: list[str] = ['typeof', 'date', 'amount', 'description']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        outcome: Outcome = self.get_object()
        return  self.request.user == outcome.owner


class OutcomeDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    Outcome Delete View\n
    name => income-delete
    """

    model = Outcome
    success_url: str = '/'

    def test_func(self) -> bool:
        outcome: Outcome = self.get_object()
        return  self.request.user == outcome.owner


# Statistics
@login_required
def statistics(request: HttpResponse) -> HttpResponse:
    """
    Statistics\n
    name => statistics
    """

    user = User.objects.filter(username = request.user).first()

    context = {
        'database_income': Income.objects.filter(owner = user),
        'database_outcome': Outcome.objects.filter(owner = user),
    }


    # Database
    database_income = context['database_income']
    database_outcome = context['database_outcome']


    # Totals
    total_income: int = get_total(database_income)
    context['total_income'] = total_income
    total_outcome: int = get_total(database_outcome)
    context['total_outcome'] = total_outcome


        # Last 7 days
    # Total Income
    total_income_last_7_days: int = get_total_last_7_days(database_income)
    context['total_7_days_income'] = total_income_last_7_days

    # Total Outcome
    total_outcome_last_7_days: int = get_total_last_7_days(database_outcome)
    context['total_7_days_outcome'] = total_outcome_last_7_days

    # Percentages 
    context['percentage_income'] = get_percentage(total_income, total_income_last_7_days)
    context['percentage_outcome'] = get_percentage(total_outcome, total_outcome_last_7_days)

        # Last 30 Days
    # Total Income
    total_income_last_30_days: int = get_total_last_30_days(database_income)
    context['total_income_last_30_days'] = total_income_last_30_days

    # Total Outcome
    total_outcome_last_30_days: int = get_total_last_30_days(database_outcome)
    context['total_outcome_last_30_days'] = total_outcome_last_30_days
    
    # Percentages 
    context['percentage_income_30'] = get_percentage(total_income, total_income_last_30_days)
    context['percentage_outcome_30'] = get_percentage(total_outcome, total_outcome_last_30_days)


        # Last 365 Days
    # Total Income
    total_income_last_365_days: int = get_total_last_365_days(database_income)
    context['total_income_last_365_days'] = total_income_last_365_days

    # Total Outcome
    total_outcome_last_365_days: int = get_total_last_365_days(database_outcome)
    context['total_outcome_last_365_days'] = total_outcome_last_365_days
    
    # Percentages 
    context['percentage_income_365'] = get_percentage(total_income, total_income_last_365_days)
    context['percentage_outcome_365'] = get_percentage(total_outcome, total_outcome_last_365_days)
    
    return render(request, 'expenses/statistics.html', context)