from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ContactForm, PortfolioItemForm, HobbyForm, RegisterForm
from .models import Hobby, PortfolioItem

def home(request):
    return render(request, 'PortfolioDatabase/home.html', {
        'welcome_message': "Welcome to my portfolio!",
        'summary': "Hi, I'm a computer science student talking about my work and hobbies."
    })

def hobbies(request):
    hobbies_list = Hobby.objects.all()
    return render(request, 'PortfolioDatabase/hobbies.html', {'hobbies': hobbies_list})

def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, pk=hobby_id)
    return render(request, 'PortfolioDatabase/hobby_detail.html', {'hobby': hobby})

@login_required
def add_hobby(request):
    if request.method == 'POST':
        form = HobbyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hobbies')
    else:
        form = HobbyForm()
    return render(request, 'PortfolioDatabase/add_hobby.html', {'form': form})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'PortfolioDatabase/portfolio.html', {'portfolio': portfolio_items})

def portfolio_detail(request, portfolio_id):
    portfolio_item = get_object_or_404(PortfolioItem, pk=portfolio_id)
    return render(request, 'PortfolioDatabase/portfolio_detail.html', {'portfolio_item': portfolio_item})

@login_required
def add_portfolio_item(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = PortfolioItemForm()
    return render(request, 'PortfolioDatabase/add_portfolio_item.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'PortfolioDatabase/contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'PortfolioDatabase/contact.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'PortfolioDatabase/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'PortfolioDatabase/register.html', {'form': form})
