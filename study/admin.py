from django.contrib import admin
from .models import Post, Comment


admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_display_links = ['id','title']
	list_filter = ['author']
	list_editable = ['author']
