from django.shortcuts import render, redirect
from .models import *
from .forms import *

from django.views import generic


# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    return render(request, 'about.html')

def SellerPage(request):
    seller = Seller.objects.all()
    context = {'seller':seller}
    return render(request, 'seller.html',context)

def SellPage(request):
    sell = Sell.objects.all()
    context = {'sell':sell}
    return render(request, 'sell.html',context)

def OrderPage(request):
    order = Order.objects.all()
    context = {'order':order}
    return render(request, 'order.html',context)

def DeliveryPage(request):
    delivery = Delivery.objects.all()
    context = {'delivery':delivery}
    return render(request, 'delivery.html',context)

def ReviewPage(request):
    review = Review.objects.all()
    queries = {'review': review}
    return render(request, "review.html", queries)

class ReviewDetail(generic.DetailView):
    model = Review
    template_name = 'review-detail.html'

def AddReview(request):
    form = CreateReview()
    if request.method == 'POST':
        item = CreateReview(request.POST)
        if item.is_valid():
            item.save()
            return redirect('review')
    value = {'form':form}
    return render(request, 'create.html',value)

def AddSeller(request):
    form = CreateSeller()
    if request.method == 'POST':
        item = CreateSeller(request.POST)
        if item.is_valid():
            item.save()
            return redirect('seller')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateSeller(request,pk):
    updateditem = Seller.objects.get(id=pk)
    form = CreateSeller(instance=updateditem)
    if request.method == "POST":
        item = CreateSeller(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('seller')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteSeller(request,pk):
    deleteitem = Seller.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('seller')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddSell(request):
    form = CreateSell()
    if request.method == 'POST':
        item = CreateSell(request.POST)
        if item.is_valid():
            item.save()
            return redirect('sell')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateSell(request,pk):
    updateditem = Sell.objects.get(id=pk)
    form = CreateSell(instance=updateditem)
    if request.method == "POST":
        item = CreateSell(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('sell')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteSell(request,pk):
    deleteitem = Sell.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('sell')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddOrder(request):
    form = CreateOrder()
    if request.method == 'POST':
        item = CreateOrder(request.POST)
        if item.is_valid():
            item.save()
            return redirect('order')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateOrder(request,pk):
    updateditem = Order.objects.get(id=pk)
    form = CreateOrder(instance=updateditem)
    if request.method == "POST":
        item = CreateOrder(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('order')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteOrder(request,pk):
    deleteitem = Order.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('order')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)

def AddDelivery(request):
    form = CreateDelivery()
    if request.method == 'POST':
        item = CreateDelivery(request.POST)
        if item.is_valid():
            item.save()
            return redirect('delivery')
    value = {'form':form}
    return render(request, 'create.html',value)

def UpdateDelivery(request,pk):
    updateditem = Delivery.objects.get(id=pk)
    form = CreateDelivery(instance=updateditem)
    if request.method == "POST":
        item = CreateDelivery(request.POST,instance=updateditem)
        if item.is_valid:
            item.save()
            return redirect('delivery')

    value = {'form':form}
    return render(request, 'create.html',value)

def DeleteDelivery(request,pk):
    deleteitem = Delivery.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('delivery')
    value = {'item':deleteitem}
    return render(request, 'create.html',value)
