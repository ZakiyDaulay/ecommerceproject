from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Name_APP' : 'TOKO HITAM,',
        'Name': 'Zakiy',
        'Class': 'KKI'
    }

    return render(request, "main.html", context)