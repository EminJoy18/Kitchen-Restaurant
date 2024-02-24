from django.contrib import admin
from .models import Menu, UserFeedback

# defining your own action
def make_unavailable(modeladmin, request, queryset):
    queryset.update(status=0)
make_unavailable.short_description = "Mark selected objects as unavailable"

def make_available(modeladmin, request, queryset):
    queryset.update(status=1)
make_available.short_description = "Mark selected objects as available"

class MenuAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Meal_type', 'status')
    actions = [make_unavailable, make_available]
    search_fields = ('Name',)
    list_filter = ('status', 'Meal_type')

# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(UserFeedback)