from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, BrandForm, SubProductForm
from members.models import Brand, Product, Sub_Category


def main_dashboard(request):
    return render(request, "main.html")

def brand_registration(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data["brand_name"]
            is_active = form.cleaned_data["is_active"]

            print("BRAND NAME :", brand_name)
            print("IS ACTIVE :", is_active)

            if Brand.objects.filter(brand=brand_name).exists():
                brand_data = Brand.objects.all()
                return render(request, "register_brand.html", {"form": form, "error": "Brand already exists!", "brands": brand_data})

            Brand.objects.create(brand=brand_name,is_active=is_active)
            brand_data = Brand.objects.all()
            form = BrandForm()
            return render(request, "register_brand.html", {"form": form, "success": "Brand Added To the System", "brands": brand_data})
    else:
        form = BrandForm()
    brand_data = Brand.objects.all()
    return render(request,"register_brand.html", {"form": form, "brands": brand_data})


def brand_update(request, brand_id):
    print("ID : ", brand_id)
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == "POST":
        print("Hello")
        brand_name = request.POST.get("brand_name")
        is_active = request.POST.get("is_active") == "on"

        print("BRAND NAME : ", brand_name)
        print("IS ACTIVE : ", is_active)

        if Brand.objects.filter(brand=brand_name).exclude(id=brand_id).exists():
            brands_data = Brand.objects.all()
            return render(request, "register_brand.html", {"brands": brands_data,"error": "Brand already exists!"})
        brand.brand = brand_name
        brand.is_active = is_active
        brand.save()
        print("Brand updated successfully")
        return redirect("brand_registration")
    return redirect("brand_registration")


def product_registration(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand_name']
            product_name = form.cleaned_data['product_name']
            is_active = form.cleaned_data['is_active']

            print("BRAND ID :", brand.id)
            print("BRAND NAME:", brand.brand)
            print("PRODUCT NAME:", product_name)
            print("IS ACTIVE:", is_active)

            if Product.objects.filter(product_name=product_name).exists():
                products_data = Product.objects.all()
                brand_data = Brand.objects.all()
                return render(request, "register_product.html",{"form": form, "error": "Product already exists", "products": products_data,"brands": brand_data })

            Product.objects.create(brand=brand,product_name=product_name,is_active=is_active)
            products_data = Product.objects.all()
            brand_data = Brand.objects.all()
            form = ProductForm()

            return render(request,"register_product.html",{"form": form, "success": "Product Added To The System","products": products_data, "brands": brand_data})
    else:
        form = ProductForm()
    products_data = Product.objects.all()
    brand_data = Brand.objects.all()

    return render(request,"register_product.html",{"form": form, "products": products_data, "brands": brand_data})

def subproduct(request):
    if request.method == "POST":
        form = SubProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product_name']
            brand = form.cleaned_data['brand_name']
            category_name = form.cleaned_data['category_name']
            price = form.cleaned_data['price']

            print("PRODUCT :", product)
            print("BRAND :", brand)
            print("CATEGORY :", category_name)
            print("PRICE :", price)

            if Sub_Category.objects.filter(category_name=category_name).exists():
                subproducts_data = Sub_Category.objects.all()
                form = SubProductForm()
                return render(request, "register_subproduct.html",{ "form": form, "error": "Category already exists", "subproducts": subproducts_data})

            Sub_Category.objects.create(product=product,brand=brand,category_name=category_name,price=price)
            subproducts_data = Sub_Category.objects.all()
            form = SubProductForm()
            return render(request, "register_subproduct.html",{"form": form, "success": "Category Added To The System","subproducts": subproducts_data})
    else:
        form = SubProductForm()
    subproducts_data = Sub_Category.objects.all()

    return render(request, "register_subproduct.html",{"form": form,"subproducts": subproducts_data })


