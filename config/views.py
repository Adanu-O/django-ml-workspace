from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Django QIT Workspace</h1>
        <ul>
            <li><a href="/rentprediction/">Rent Prediction</a></li>
            <li><a href="/leetcode/">LeetCode Practice</a></li>
            <li><a href="/qitsol/">QIT Solutions</a></li>
        </ul>
    """)
