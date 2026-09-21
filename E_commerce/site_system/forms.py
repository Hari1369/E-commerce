from django import forms
from datetime import datetime, date
from django.utils.timezone import now
import datetime
from members.models import Product, Sub_Category, Brand



class BrandForm(forms.Form):
    brand_name = forms.CharField(max_length=255)
    is_active = forms.BooleanField(required=False, initial=True)


class ProductForm(forms.Form):
    brand_name = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=True,
        empty_label="Select Brand"
    )

    product_name = forms.CharField(max_length=255)

    is_active = forms.BooleanField(
        required=False,
        initial=True
    )


class SubProductForm(forms.Form):
    product_name = forms.ModelChoiceField(queryset=Product.objects.all(),required=True, empty_label="Select Brand")
    brand_name = forms.ModelChoiceField(queryset=Brand.objects.all(),required=True, empty_label="Select Brand")
    category_name = forms.CharField(max_length=255, required=True)
    price = forms.IntegerField(required=True)




