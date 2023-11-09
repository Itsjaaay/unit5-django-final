from django.shortcuts import render
from django.http import HttpResponse

def hey(request, name):
    return HttpResponse(f'Hey, {name.capitalize()}!')




from django.http import HttpResponse

def age_in(request, end, birthyear):
    age = int(end) - int(birthyear)
    return HttpResponse(str(age))



from django.http import HttpResponse

def order_total(request, burgers, fries, drinks):
    burger_price = 4.50
    fries_price = 1.50
    drinks_price = 1.00
    total = (burgers * burger_price) + (fries * fries_price) + (drinks * drinks_price)
    return HttpResponse(f'Total Order Amount: ${total:.2f}')
