from django.shortcuts import render, redirect
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
 
def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={"categories": TutorialCategory.objects.all})
                  
def register(request):
   if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           user = form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f"New account created: {username}")
           login(request, user)
           return redirect("homepage")
 
       else:
           for msg in form.error_messages:
               messages.error(request, f"{msg}: {form.error_messages[msg]}")
 
           return render(request = request,
                         template_name = "register.html",
                         context={"form":form})
 
   form = UserCreationForm
   return render(request = request,
                 template_name = "register.html",
                 context={"form":form})


# we will ust the django internal login and logout they are easy to use
def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
      return HttpResponse(f"{single_slug} is a category")

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
      return HttpResponse(f"{single_slug} is a Tutorial")

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")