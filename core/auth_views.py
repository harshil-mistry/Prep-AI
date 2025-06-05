from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import uuid
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful signup
    template_name = 'signup.html'

class CustomLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'signin.html'
    redirect_authenticated_user = True  # Redirect authenticated users to success_url
    
    def get_success_url(self):
        return reverse_lazy('chat') # Redirect to chat page after successful login

def quick_login(request):
    if request.method == 'POST':
        """Single-click login for development purposes"""
        # Generate a unique username for this session
        unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
        
        # Create a new user for this session
        user = User.objects.create_user(
            username=unique_username,
            email=f"{unique_username}@example.com",
            password='testpass123'
        )
        
        # Log the user in
        login(request, user)
        return redirect('chat')

    return render(request, 'login.html')

def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('login') # Redirect to the new login page after logout 