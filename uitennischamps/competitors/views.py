from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader 
from django.contrib import messages
from django.contrib.auth import authenticate, login

def my_view(request):
    # Example view function
    messages.success(request, 'This is a success message.')
    messages.error(request, 'This is an error message.')
    return render(request, 'my_template.html')


# Create your views here.
def index_view(request):
    index_template = loader.get_template('index.html')
    return HttpResponse(index_template.render())

def match_view(request):
    match_temp = loader.get_template('new_match.html')
    return HttpResponse(match_temp.render())

def biodata_form(request):
    bio_template = loader.get_template('biodata_form.html')
    return HttpResponse(bio_template.render())

def player_view(request):
    template = loader.get_template('new_player.html')
    return HttpResponse(template.render())

def match_details_view(request):
    template = loader.get_template('get_match_detail.html')
    return HttpResponse(template.render())

def base_view(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def score_view(request):
    template = loader.get_template('add_score.html')
    return HttpResponse(template.render())

def contact_form(request):
    bio_template = loader.get_template('contact_form.html')
    return HttpResponse(bio_template.render())

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if user.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
            else:
                user = user.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                messages.success(request, 'You have successfully signed up.')
                return redirect('index')  # Redirect to home page or another page
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'signup.html')

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('index')  # Redirect to home page or another page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'signin.html')