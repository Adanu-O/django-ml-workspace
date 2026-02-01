from django.shortcuts import render
from .utils import substring

# Create your views here.
from django.http import HttpResponse

def leet_home(request):
    #return HttpResponse("Hello from App2 - Leetcode solution")

    return HttpResponse("""
        <h1>Leetcode solution - substring lenght of non-repeating characters</h1>
        <ul>
            <li><a href="/leetcode/substring/">lengthOfLongestSubstring</a></li>
        </ul>
        <br>
        <a href="/">⬅ Back to Main Page</a>
    """)

from django.http import JsonResponse
from .utils import substring    
    
def substring_view(request):
    s = request.GET.get("a")
    #b_str = request.GET.get("b")

    if not s:
        return JsonResponse(
            {"error": "Provide a string of characters. Or use the following link to test or change the characters at the end of the link: http://127.0.0.1:8000/leetcode/substring/?a=kalakuta"},
            status=400
        )



    if len(s) > 30:
        return JsonResponse(
            {"error": "Length of character should not exceed 30. This is for testing purpose only please."},
            status=400
        )

    result = substring(s)

    return JsonResponse({
        "Input": s,
        
        "Substring lenght of non-repeating characters": result
    })
