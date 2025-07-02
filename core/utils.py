import os
import hmac
import hashlib
import time
from django.conf import settings
from django.http import HttpResponseForbidden, JsonResponse

def generate_auth_token():
    """Generate a time-based authentication token"""
    timestamp = str(int(time.time()))
    message = f"{timestamp}:{settings.SECRET_KEY}"
    signature = hmac.new(
        settings.SECRET_KEY.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    return f"{timestamp}:{signature}"

def verify_auth_token(token):
    """Verify the authentication token"""
    try:
        timestamp, signature = token.split(':')
        timestamp = int(timestamp)
        
        # Check if token is expired (5 minutes validity)
        if time.time() - timestamp > 300:
            return False
            
        message = f"{timestamp}:{settings.SECRET_KEY}"
        expected_signature = hmac.new(
            settings.SECRET_KEY.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        
        return hmac.compare_digest(signature, expected_signature)
    except:
        return False

def verify_request_origin(request):
    """Verify that the request is coming from our frontend"""
    # Get the origin from the request
    origin = request.headers.get('Origin', '')
    referer = request.headers.get('Referer', '')
    
    # List of allowed origins (add your frontend domains)
    allowed_origins = [
        'http://localhost:8000',
        'http://127.0.0.1:8000',
        'https://prep-ai-sq31.onrender.com'
    ]
    
    # Check if the request is coming from an allowed origin
    if origin in allowed_origins or any(referer.startswith(origin) for origin in allowed_origins):
        return True
    return False

def require_auth(view_func):
    """Decorator to require authentication for views"""
    def wrapper(request, *args, **kwargs):
        # Skip authentication for GET requests
        if request.method == 'GET':
            return view_func(request, *args, **kwargs)
            
        # Verify request origin
        if not verify_request_origin(request):
            return JsonResponse({'success': False, 'error': 'Invalid request origin'}, status=403)
            
        # Get the auth token from the request
        auth_token = request.headers.get('X-Auth-Token')
        if not auth_token or not verify_auth_token(auth_token):
            return JsonResponse({'success': False, 'error': 'Invalid authentication token'}, status=403)
            
        return view_func(request, *args, **kwargs)
    return wrapper 