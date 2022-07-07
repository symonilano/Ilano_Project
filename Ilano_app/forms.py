from django.forms import ModelForm
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateSeller(ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'

class CreateSell(ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'

class CreateOrder(ModelForm):
    class Meta:
        widgets = {'Order_Date':DateInput()}
        model = Order
        fields = '__all__'

class CreateDelivery(ModelForm):
    class Meta:
        widgets = {'Delivery_Date':DateInput()}
        model = Delivery
        fields = '__all__'

class CreateReview(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
