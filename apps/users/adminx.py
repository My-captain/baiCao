import xadmin
from xadmin import views

from .models import UserProfile, Base, Banner, News, Staff


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "百草"
    site_footer = "百草\n" \
                  "小可爱"
    menu_style = "accordion"


class BaseAdmin(object):
    list_display = ['name', 'address', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class BannerAdmin(object):
    list_display = ['index', 'content', 'add_time']
    search_fields = ['index']
    list_filter = ['index', 'add_time']


class NewsAdmin(object):
    list_display = ['title', 'content', 'author', 'add_time']
    search_fields = ['author']
    list_filter = ['author', 'add_time']


class StaffAdmin(object):
    list_display = ['name', 'mobile_phone', 'salary', 'seniority', 'add_time']
    search_fields = ['name', 'seniority', 'salary']
    list_filter = ['salary', 'seniority', 'add_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Base, BaseAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(Staff, StaffAdmin)
