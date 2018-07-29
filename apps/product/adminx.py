import xadmin

from .models import Goods, Plants


class GoodsAdmin(object):
    list_display = ['name', 'type', 'count', 'price', 'base', 'add_time']
    search_fields = ['customer', 'staff']
    list_filter = ['type', 'base', 'add_time']
    list_export = ['xls', 'csv', 'xml', 'json']
    show_all_rel_details = True
    list_editable = "__all__"


class PlantsAdmin(object):
    list_display = ['name', 'classes', 'specification', 'medicinal_parts', 'flavour', 'image', 'add_time']
    search_fields = ['name', 'classes', 'specification', 'medicinal_parts', 'flavour']
    list_filter = ['classes', 'specification', 'medicinal_parts', 'flavour', 'add_time']


xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Plants, PlantsAdmin)

