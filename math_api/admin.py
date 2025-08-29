from django.contrib import admin
from django.utils.html import format_html
from .models import AppUser, MathQuery, UserSearch

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('udid', 'token', 'created_at')
    search_fields = ('udid',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


# @admin.register(MathQuery)
# class MathQueryAdmin(admin.ModelAdmin):
    # list_display = ('user', 'question', 'created_at')
    # search_fields = ('user__udid', 'question')
    # list_filter = ('created_at',)
    # readonly_fields = ('image_preview', 'created_at')

    # fieldsets = (
        # (None, {
            # 'fields': ('user', 'question', 'answer', 'created_at', 'image_preview')
        # }),
    # )

    # def image_preview(self, obj):
        # if obj.image_base64:
            # return format_html('<img src="data:image/jpeg;base64,{}" width="200" />', obj.image_base64)
        # return "-"
    # image_preview.short_description = 'Image Preview' 


@admin.register(UserSearch)
class UserSearchAdmin(admin.ModelAdmin):
    list_display = ('user', 'input_type', 'short_prompt', 'created_at', 'updated_at')
    search_fields = ('user__udid', 'prompt', 'response')
    list_filter = ('input_type', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    def short_prompt(self, obj):
        return obj.prompt[:500] + "..." if obj.prompt and len(obj.prompt) > 500 else obj.prompt
    short_prompt.short_description = 'Prompt'

    def image_preview(self, obj):
        if obj.input_type == 'image' and obj.prompt:  # assuming prompt contains base64 image data or URL
            if obj.prompt.startswith('data:image'):  # base64 string
                return format_html('<img src="{}" width="200" />', obj.prompt)
            elif obj.prompt.startswith('http'):  # remote image URL
                return format_html('<img src="{}" width="200" />', obj.prompt)
        return "-"
    image_preview.short_description = 'Image Preview'