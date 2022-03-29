from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GoodForm, EditGoodDescriptionForm, ReviewForm, LoginForm, RegisterForm
from .models import Good, Review


@login_required
def add_good(request):
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            good = Good.objects.create(**form.cleaned_data)
            return redirect('good_detail', good.id)
    else:
        form = GoodForm()
        return render(request, 'form.html', {'form': form})


@login_required
def edit_good(request, good_id):
    if request.method == 'POST':
        form = EditGoodDescriptionForm(request.POST)
        if form.is_valid():
            good = get_object_or_404(Good, pk=good_id)
            good.description = form.cleaned_data["description"]
            good.save()
            return redirect('good_detail', good.id)
    else:
        form = EditGoodDescriptionForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_review(request, good_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            good = get_object_or_404(Good, pk=good_id)
            Review.objects.create(good=good, user=user, **form.cleaned_data)
            return redirect('good_review_list', good.id)
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('good_review_list', review.good.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.save()
                return redirect('good_review_list', review.good.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def good_detail(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    return render(request, 'good_detail.html', {'good': good})


def good_list(request):
    goods = Good.objects.all()
    return render(request, 'good_list.html', {'goods': goods})


def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


def good_review_list(request, good_id):
    reviews = Review.objects.filter(good=good_id)
    return render(request, 'review_list.html', {'reviews': reviews})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "form.html", {"form": form})