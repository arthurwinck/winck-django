from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','user',)
    list_filter = ('date','user')
    exclude = ('slug',)
    search_fields = ('title','body',)

    class Meta:    
        model = Posts