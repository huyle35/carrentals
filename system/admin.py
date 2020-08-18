from django.contrib import admin
from .models import Car, Order, PrivateMsg, Quote, Customer
# Register your models here.

class CarAdmin(admin.ModelAdmin):

    list_display = ("hình_ảnh",
                    "tên_xe",
                    "tên_công_ty",
                    "số_ghế",
                    "giá_tham_khảo",
                    "nội_dung",)
                    
class OrderAdmin(admin.ModelAdmin):

    list_display = ("tên_xe",
                    "tên_khách_hàng",
                    "ngày_đi",
                    "ngày_về",
                    "xuất_phát",
                    "điểm_đến",
                    )

class PrivateMsgAdmin(admin.ModelAdmin):

    list_display = ("tên_người_dùng", 
                    "số_điện_thoại",
                    "email", 
                    "nội_dung")

class QuoteAdmin(admin.ModelAdmin):

    list_display = ("số_điện_thoại",
                    "tên_xe",
                    "ngày_đi",
                    "ngày_về",
                    "xuất_phát",
                    "điểm_đến",)      

class CustomerAdmin(admin.ModelAdmin):
    
    list_display = ("tên_khách_hàng",
                    "số_điện_thoại",
                    "địa_chỉ",
                    )                   

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Customer, CustomerAdmin)