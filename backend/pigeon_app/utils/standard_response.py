from django.http import JsonResponse
def StandardJsonResponse(input):
    return JsonResponse({'message': input })