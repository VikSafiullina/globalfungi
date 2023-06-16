from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Send confirmation email
            send_confirmation_email(user)

            return redirect('home')  # Redirect to the home page or any desired page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def send_confirmation_email(user):
    subject = 'Confirm Your Registration'
    message = f'Hi {user.username}, thank you for registering. Please confirm your email address.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any desired page
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    return render(request, 'registration/login.html')


from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            timestamp = form.cleaned_data['timestamp']
            
            # Save or process the form data as required

            # Render success page or redirect to a success URL
            return render(request, 'success.html')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def faq(request):
    return render(request, 'faq.html')


def handler_404(request, exception):
    return render(request, '404.html', {})