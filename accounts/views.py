from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SignUpForm


# Using FBVs for now.
def signup_view(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("home"))

    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)
