from django.contrib import admin
from .models import Article


# Register your models here.

class MultiDBModelAdmin(admin.ModelAdmin):

    DB_name = 'db_article_wiki'

    def save_model(self, request, obj, form, change):

        obj.save(using=self.DB_name)

    def delete_model(self, request, obj):

        obj.delete(using=self.DB_name)

    def get_queryset(self, request):

        return super().get_queryset(request).using(self.DB_name)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        return super().formfield_for_foreignkey(db_field, request, using=self.DB_name, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):

        return super().formfield_for_manytomany(db_field, request, using=self.DB_name, **kwargs)


admin.site.register(Article,MultiDBModelAdmin)