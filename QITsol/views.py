from django.shortcuts import render
from django.http import HttpResponse
from .utils import inner_product
import numpy as np


def qitsol_home(request):
    return HttpResponse("""
        <h1>QIT Solutions Tools</h1>
        <ul>
            <li><a href="/qitsol/inner_product/">Inner Product Calculator</a></li>
        </ul>
        <br>
        <a href="/">⬅ Back to Main Page</a>
    """)


from django.http import JsonResponse
from .utils import inner_product

def inner_product_view(request):
    a_str = request.GET.get("a")
    b_str = request.GET.get("b")

    if not a_str or not b_str:
        return JsonResponse(
            {"error": "Provide a and b as query parameters. Or use the following link to test or change the values at the end of the link: http://127.0.0.1:8000/qitsol/inner_product/?a=1,2,3&b=4,5,6"},
            status=400
        )

    try:
        a = list(map(float, a_str.split(",")))
        b = list(map(float, b_str.split(",")))
    except ValueError:
        return JsonResponse(
            {"error": "a and b must be numbers"},
            status=400
        )

    if len(a) != len(b):
        return JsonResponse(
            {"error": "Vectors must have the same length"},
            status=400
        )

    result = inner_product(a, b)

    return JsonResponse({
        "a": a,
        "b": b,
        "inner_product": result
    })







