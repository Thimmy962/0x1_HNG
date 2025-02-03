from django.http import JsonResponse
from . import func



def index(request):
    num = request.GET.get("number")
    if not num:
        return JsonResponse({'error': 'Number parameter is required'}, status=400)
    try:
        num = int(num)
    except ValueError:
        error_data = {
                "number": "alphabet",
                "error": "true"
                }
        return JsonResponse(error_data, safe = False, status = 400)
    fun_fact = func.fun_fact(num)
    if  fun_fact == 500:
        fun_fact = "Could not get fun_fact for number as connection timed out"
        
    data = {
        "number": num,
        "is_prime": func.is_prime_num(num),
        "is_perfect": func.is_perfect(num),
        "properties": [func.is_armstrong(num), func.is_even_or_odd(num)],
        "digit_sum": func.digit_sum(num),
        "fun_fact": fun_fact
    }
    return JsonResponse(data, safe=False, status=200) 