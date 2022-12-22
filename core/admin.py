from django.contrib import admin
from . import models


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(models.Task)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["title", "organization", "segmentation"]


@admin.register(models.Realization)
class RealizationAdmin(admin.ModelAdmin):
    list_display = ["account", "organization", "task", "status", "points"]
