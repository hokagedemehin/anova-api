from django.contrib import admin
from .models import Bids, BidsHistory
# Register your models here.

class BidsAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    list_filter = ('user__first_name', 'user__last_name', 'user__email', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    search_fields = ('user', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    list_per_page = 25

    class Meta:
        verbose_name_plural = 'Bids'
        ordering = ['-created_at']

admin.site.register(Bids, BidsAdmin)

class BidsHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    list_filter = ('user__first_name', 'user__last_name', 'user__email', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    search_fields = ('user', 'quantity', 'price', 'start_time', 'close_time', 'created_at', 'updated_at')
    list_per_page = 25

    class Meta:
        verbose_name_plural = 'BidsHistory'
        ordering = ['-created_at']

admin.site.register(BidsHistory, BidsHistoryAdmin)