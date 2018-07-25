import xadmin

from .models import Goods, Plants


class GoodsAdmin(object):
    list_display = ['name', 'type', 'count', 'price', 'base', 'add_time']
    search_fields = ['customer', 'staff']
    list_filter = ['type', 'base', 'add_time']


class PlantsAdmin(object):
    list_display = ['name', 'classes', 'specification', 'parts', 'flavour', 'add_time']
    search_fields = ['name', 'classes', 'specification', 'parts', 'flavour']
    list_filter = ['classes', 'specification', 'parts', 'flavour', 'add_time']


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Plants, PlantsAdmin)

