from django.contrib import admin
from models import Project, ProjectScreenshot
# Register your models here.

class PortfolioImageInline(admin.TabularInline):
    model = ProjectScreenshot
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageInline]

admin.site.register(Project, ProjectAdmin)

# Hello little buddy
