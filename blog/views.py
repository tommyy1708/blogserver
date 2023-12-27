# blog/views.py
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



def fetch_username(request):
    if request.method == 'POST':
        # Get the 'username' value from the POST data
        username = request.POST.get('username')

        # Check if the 'username' value is present
        if username:
            # Process the username as needed
            # For example, you can query the 'users' table using the username
            # Here, we'll just return the username in a JsonResponse
            return JsonResponse({'username': username})
        else:
            return JsonResponse({'error': 'Username not provided'}, status=400)

    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'}, status=405)
