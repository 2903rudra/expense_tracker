from django.shortcuts import render,redirect

# Create your views here.
from .forms import ExpenseForm
from .models import Expense

from django.db.models import Sum

import datetime

def index(request):

    if request.method == "POST":
        expense = ExpenseForm(request.POST)

        if expense.is_valid():
            expense.save()

    expense_form = ExpenseForm()

    return render(request,'expense_app/index.html',{'expense_form':expense_form})

def show_expenses(request):
    expenses = Expense.objects.all()
    total_expense = expenses.aggregate(Sum('amount'))

    # logic to calculate last 365days expense

    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt = last_year)
    yearly_sum = data.aggregate(Sum('amount'))

    # logic to calculate last 30days expense

    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt = last_month)
    monthly_sum = data.aggregate(Sum('amount'))

    # logic to calculate last 7 days expense

    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt = last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    # daily sums

    daily_sums = Expense.objects.filter().values('date').order_by('date').annotate(Sum('amount'))

    # categorical filter

    categorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(Sum('amount'))

    return render(request,'expense_app/expense.html',{'expenses' : expenses,'total_expenses' : total_expense,'yearly_sum' : yearly_sum,'monthly_sum' : monthly_sum,'weekly_sum' : weekly_sum,'daily_sums' : daily_sums,'categorical_sums' : categorical_sums})


def edit(request,id):
    expense = Expense.objects.get(id=id)
    form = ExpenseForm(instance=expense)

    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('expense')

    return render(request,'expense_app/edit.html',{'expense_form' : form})


def delete(request,id):
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        expense.delete()

    return redirect('expense')