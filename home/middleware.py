from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware to restrict access to specific pages unless the user is authenticated.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = [
            reverse('about'),  # Adjust the view names to match your URL configuration
            reverse('services'),
            reverse('dashboard'),
            reverse('contact'),
        ]
        if request.path in restricted_paths and not request.user.is_authenticated:
            return redirect('login')  # Redirect to the login page if not authenticated
        return self.get_response(request)
