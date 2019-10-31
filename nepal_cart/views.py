from django.shortcuts import render


def search(request):
    return render(request, template_name='index.html')

def about(request):
    return render(request, template_name='pages/about.html')

def blog(request):
    return render(request, template_name='pages/blog.html')

def boy(request):
    return render(request, template_name='pages/boy.html')

def boys(request):
    return render(request, template_name='pages/boys.html')

def checkout(request):
    return render(request, template_name='pages/checkout.html')

def contact(request):
    return render(request, template_name='pages/contact.html')

def faq(request):
    return render(request, template_name='pages/faq.html')

def girl(request):
    return render(request, template_name='pages/girl.html')

def girls(request):
    return render(request, template_name='pages/girls.html')

def men(request):
    return render(request, template_name='pages/men.html')

def mens(request):
    return render(request, template_name='pages/mens.html')

def payment(request):
    return render(request, template_name='pages/payment.html')

def single(request):
    return render(request, template_name='pages/single.html')

def shop(request):
    return render(request, template_name='pages/shop.html')

def women(request):
    return render(request, template_name='pages/women.html')

def womens(request):
    return render(request, template_name='pages/womens.html')

