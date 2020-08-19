from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
from .models import Car, Order, PrivateMsg, User, Quote, Customer
from .forms import CarForm, OrderForm, MessageForm, QuoteForm, ProfileForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import user_passes_test


def home(request):
    context = {
        "title" : "Hoàng Gia Thịnh"
    }
    return render(request,'home.html', context)

    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/carlist/")
    return render(request,'home.html')

def car_list(request):
    car = Car.objects.all()

    query = request.GET.get('q')
    if query:
        car = car.filter(
                     Q(tên_xe__icontains=query) |
                     Q(tên_công_ty__icontains = query) |
                     Q(số_ghế__icontains=query) |
                     Q(giá_tham_khảo__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'car_list.html', context)

def car_detail(request, id=None):
    detail = get_object_or_404(Car,id=id)
    context = {
        "detail": detail
    }
    return render(request, 'car_detail.html', context)

def car_created(request):
    form = CarForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/auth")
    context = {
        "form" : form,
        "title": "Thêm Xe Mới"
    }
    return render(request, 'car_create.html', context)

def car_update(request, id=None):
    detail = get_object_or_404(Car, id=id)
    form = CarForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/auth")
    context = {
        "form": form,
        "title": "Chỉnh Sửa Xe"
    }
    return render(request, 'car_create.html', context)

def car_delete(request,id=None):
    query = get_object_or_404(Car,id = id)
    query.delete()

    car = Car.objects.all()
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)

#order

def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(tên_xe__icontains=query)|
            Q(tên_khách_hàng__icontains=query)|
            Q(số_điện_thoại__icontains=query)
        )
    
    # pagination
    paginator = Paginator(order, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'order': order,
    }
    return render(request, 'order_list.html', context)

def order_detail(request, id=None):
    detail = get_object_or_404(Order,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)

def order_created(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
        "title": "Tạo đơn đặt xe"
    }
    return render(request, 'order_create.html', context)

def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Thay đổi đơn đặt xe"
    }
    return render(request, 'order_create.html', context)

def order_delete(request,id=None):
    query = get_object_or_404(Order,id = id)
    query.delete()
    return render(request, 'order_delete.html')

def newcar(request):
    new = Car.objects.order_by('-id')
    #seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(tên_xe__icontains=query) |
            Q(tên_công_ty__icontains=query) |
            Q(số_ghế__icontains=query) |
            Q(giá_tham_khảo__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)

def like_update(request, id=None):
    new = Car.objects.order_by('-id')
    like_count = get_object_or_404(Car, id=id)
    like_count.lượt_thích+=1
    like_count.save()
    context = {
        'car': new,
    }
    return render(request,'new_car.html',context)

def popular_car(request):
    new = Car.objects.order_by('-lượt_thích')
    # seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(tên_xe__icontains=query) |
            Q(tên_công_ty__icontains=query) |
            Q(số_ghế__icontains=query) |
            Q(giá_tham_khảo__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'car': new,
    }
    return render(request, 'new_car.html', context)

def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/car/newcar/")
    context = {
        "form": form,
        "title": "Liên Hệ",
    }
    return render(request,'contact.html', context)

def quote(request):
    form = QuoteForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request,'quote_success.html')
    context = {
        "form": form,
        "title": "Quote",
    }
    return render(request,'quote.html', context)

def profile_update(request, id=None):
    if request.user.is_authenticated:
        profile = User.objects.get(id=id)
        form = ProfileForm(request.POST or None, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return render(request, 'profile_update.html')
        context = {
            "form": form,
            "title": "Thay đổi thông tin"
        }
        return render(request, 'profile.html', context)

def customer_profile(request, id=None):
    profile = Customer.objects.get(user_id = request.user.id)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.save()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)
#-----------------Admin Section-----------------
@user_passes_test(lambda u: u.is_superuser)
def admin_car_list(request):
    car = Car.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        car = car.filter(
            Q(tên_xe__icontains=query) |
            Q(tên_công_ty__icontains=query) |
            Q(số_ghế__icontains=query) |
            Q(giá_tham_khảo__icontains=query)
        )

    # pagination
    paginator = Paginator(car, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        car = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        car = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        car = paginator.page(paginator.num_pages)
    context = {
        'car': car,
    }
    return render(request, 'admin_index.html', context)

def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        msg = msg.filter(
            Q(tên_người_dùng__icontains=query) |
            Q(email__icontains=query)
        )

    # pagination
    paginator = Paginator(msg, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        msg = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        msg = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        msg = paginator.page(paginator.num_pages)
    context={
        "msg": msg,
    }
    return render(request, 'admin_msg.html', context)

def admin_quote(request):
    quote = Quote.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        quote = quote.filter(
            # Q(tên_xe__icontains=query) |
            Q(số_điện_thoại__icontains=query)
        )

    # pagination
    paginator = Paginator(quote, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        quote = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quote = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quote = paginator.page(paginator.num_pages)
    context={
        "quote": quote,
    }
    return render(request, 'admin_quote.html', context)

def admin_customer(request):
    profile = Customer.objects.order_by('-id')
    query = request.GET.get('q')
    if query:
        profile = profile.filter(
            # Q(tên_xe__icontains=query) |
            Q(số_điện_thoại__icontains=query)
        )

    # pagination
    paginator = Paginator(profile, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        profile = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profile = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profile = paginator.page(paginator.num_pages)
    context={
        "profile": profile,
    }
    return render(request, 'admin_customer.html', context)

def msg_delete(request,id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")

def quote_delete(request,id=None):
    query = get_object_or_404(Quote, id=id)
    query.delete()
    return HttpResponseRedirect("/adminquote/")
