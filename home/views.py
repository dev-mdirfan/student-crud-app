from django.shortcuts import render, redirect
from .models import User, get_state_name, STATE_CHOICES
from .forms import UserForm
# Create your views here.

# Home Page
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
        "STATE_CHOICES": STATE_CHOICES,
        # 'get_state_display': get_state_name,
    }
    return render(request, "home/index.html", context)

# Update Page
def update(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
    context = {
        "form": form,
    }
    return render(request, "home/update.html", context)

# Delete Record
def delete(request, id):
    if request.method == "POST":
        user = User.objects.get(pk=id)
        user.delete()
    return redirect("home")


