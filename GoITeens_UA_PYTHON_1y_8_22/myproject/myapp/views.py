from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Dish, Review, Table
from .forms import RegisterForm, LoginForm, ReviewForm
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .forms import TableReservationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile, TableReservation


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def dishes_demo(request):
    dishes = Dish.objects.all()
    return render(request, 'main.html', {'dishes': dishes})


@login_required
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews})


@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def reserve_table(request):
    if request.method == 'POST':
        form = TableReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            send_to_telegram(reservation)

            return redirect('dishes')
    else:
        form = TableReservationForm()
    return render(request, 'reserve_table.html', {'form': form})


def send_to_telegram(reservation):
    bot_token = settings.BOT_TOKEN
    chat_id = settings.CHAT_ID
    message = f'New table reservation:\nName: {reservation.first_name} {reservation.last_name}\nPhone: {reservation.phone_number}\nTable: {reservation.table_number}'
    requests.post(f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}')