# def fetch_username(request):
#     if request.method == 'GET':
#           with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM users")
#             user_data = cursor.fetchone()

#           # Query the database to get the user's profile
#           if user_data:
#             return JsonResponse({'data':user_data})
#           else:
#             return JsonResponse({'error': 'User not found'}, status=404)
#     # Handle other HTTP methods if needed
#     return JsonResponse({'error': 'Invalid request method'}, status=405)

from django.db import connection
from django.http import JsonResponse

def fetch_all_users(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            columns = [col[0] for col in cursor.description]
            user_data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Query the database to get all user profiles
        if user_data:
            return JsonResponse({'data': user_data})
        else:
            return JsonResponse({'error': 'No users found'}, status=404)
    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'}, status=405)

