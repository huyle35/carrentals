from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
from .models import Car, Order, PrivateMsg, User, Quote, Customer, Category
from .forms import CarForm, OrderForm, MessageForm, QuoteForm, ProfileForm
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings 
import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_order_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="order.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Order')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'Tên Khách Hàng', 'Xe ID', 'Từ ngày', 'Đến ngày','Xuất phát', 'Điểm đến']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Order.objects.all().values_list('id', 'tên_khách_hàng', 'tên_xe', 'ngày_đi', 'ngày_về', 'xuất_phát', 'điểm_đến')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_car_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="car.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Car')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'Danh Mục', 'Tên xe', 'Tên Công Ty', 'Số Ghế','Giá Tham Khảo', 'Nội Dung', 'Lượt thích']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Car.objects.all().values_list('id', 'danh_mục', 'tên_xe', 'tên_công_ty', 'số_ghế', 'giá_tham_khảo', 'nội_dung', 'lượt_thích')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_quote_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="baogia.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('BaoGia')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['id', 'Số Điện Thoại', 'Xe ID', 'Từ ngày', 'Đến ngày','Xuất phát', 'Điểm đến']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Quote.objects.all().values_list('id', 'số_điện_thoại', 'tên_xe', 'ngày_đi', 'ngày_về', 'xuất_phát', 'điểm_đến')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def home(request):
    car = Car.objects.order_by("-lượt_thích")[:4]
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/contact/")
    context = {
        "form": form,
        "title" : "Hoàng Gia Thịnh",
        "car": car,
    }
    return render(request,'home.html', context)

def car_list(request):
    car = Car.objects.filter(status=True)
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

class CategoryView(View):
    def get(self, *args, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        car = Car.objects.filter(category=category)
        context = {
            'object_list': car,
            'category_title': category.danh_mục,
            'category_description': category.mô_tả,
            'category_image': category.image
        }
        return render(self.request, "car_list.html", context)

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
        Car.objects.get(id=form.tên_xe)
        instance.save()
        subject = "Hoàng Gia Thịnh"
        message = f"""Xin chào {instance.tên_khách_hàng}. 
    Chúng tôi đã nhận được đơn thuê xe của bạn.
    Bạn đã đặt xe {instance.tên_xe}
    Đi từ {instance.xuất_phát}
    Đến {instance.điểm_đến}
    Từ ngày {instance.ngày_đi} đến {instance.ngày_về}

    --- Hoàng Gia Thịnh sẽ xác nhận đơn đặt xe của bạn sau khi thanh toán thành công ---

    Mọi thắc mắc xin liên hệ: 
        + Email: info.hoanggiavn@gmail.com
        + Số điện thoại: +09 38.358.309
                   Hoặc: +09 38.100.229"""
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)
        return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        "form": form,
        "title": "Tạo đơn đặt xe"
    }
    return render(request, 'order_create.html', context)

# connection.close()

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
    new = Car.objects.order_by('-id').filter(status=True)
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
        subject = "Hoàng Gia Thịnh"
        message = f"""Xin chào số điện thoại: {instance.số_điện_thoại}. 
    Chúng tôi đã nhận được tin nhắn báo giá của bạn.
    Bạn đã đặt xe {instance.tên_xe}
    Đi từ {instance.xuất_phát}
    Đến {instance.điểm_đến}
    Từ ngày {instance.ngày_đi} đến {instance.ngày_về}

    --- Hoàng Gia Thịnh sẽ liên lạc cho trong thời gian sớm nhất.---

    Mọi thắc mắc xin liên hệ: 
        + Email: info.hoanggiavn@gmail.com
        + Số điện thoại: +09 38.358.309
                   Hoặc: +09 38.100.229"""
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email, fail_silently=True)
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

@login_required(login_url='/login/')
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

@login_required
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

@login_required
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

@login_required
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
