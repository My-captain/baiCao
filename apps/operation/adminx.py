import xadmin

from .models import Generation, Purchase, Favorite


class GenerationAdmin(object):
    list_display = ['customer', 'staff', 'begin', 'end', 'price']
    search_fields = ['customer', 'staff', ]
    list_filter = ['begin', 'end', 'price', 'deliver_type', 'plant_type']


class PurchaseAdmin(object):
    list_display = ['customer', 'goods', 'count', 'total_money', 'state']
    search_fields = ['customer', 'goods', 'state']
    list_filter = ['customer', 'goods', 'count', 'total_money', 'state']


class FavoriteAdmin(object):
    list_display = ['user', 'good', 'add_time']
    search_fields = ['user', 'good']
    list_filter = ['user', 'good', 'add_time']


xadmin.site.register(Generation, GenerationAdmin)
xadmin.site.register(Purchase, PurchaseAdmin)
xadmin.site.register(Favorite, FavoriteAdmin)

