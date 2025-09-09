from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406434102',
        'name': 'Naomi Kyla Zahra Siregar',
        'class': 'PBP B',
    }
    return render(request, "main.html", context)

