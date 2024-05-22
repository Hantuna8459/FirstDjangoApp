from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Users
from .forms import UserForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world")

def list(request):
    users = Users.objects.all()
    template_name = 'information/user_list.html'
    context = {'users':users}
    return render(request, template_name, context)

def create(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid. Saving data to the database...")
            form.save()
            return redirect('user_list')
        else:
            print ("form is invalid")
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Field: {field} - Error: {error}")   
    template_name = 'information/user_create.html'
    context = {'form':form}
    return render(request, template_name, context)

def detail(request, pk):
    user = get_object_or_404(Users, id=pk)
    template_name = 'information/user_detail.html'
    context = {'user':user}
    return render(request, template_name, context)
    
def update(request, pk):
   user = get_object_or_404(Users, id=pk)
   form = UserForm()
   if request.method == 'POST':
       form = UserForm(request.POST, request.FILES, instance=user)
       if form.is_valid():
           form.save()
           return redirect('user_list')
   template_name = 'information/user_update.html'
   context = {'form':form}
   return render(request, template_name, context)

def delete(request, pk):
    user = get_object_or_404(Users, id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    template_name = 'information/user_confirm_delete.html'
    context = {'user':user}
    return render(request, template_name, context)