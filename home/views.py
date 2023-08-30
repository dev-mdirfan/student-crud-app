from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
# Create your views here.

def home(request):
    users = User.objects.all()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserForm()
    context = {
        "users": users,
        "form": form,
    }
    return render(request, "home/index.html", context)

def update(request, id):
    return render(request, "home/update.html")

def delete(request, id):
    return redirect("home")


