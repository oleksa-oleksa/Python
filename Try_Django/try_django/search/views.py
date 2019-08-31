from django.shortcuts import render


# Create your views here.
def search_view(request):
    return render(request, 'searches/view.html', {})