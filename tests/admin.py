from django.contrib import admin

# Register your models here.
from tests.models import Test, Task, Variant, Assignment


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class TestAssignmentAdmin(admin.ModelAdmin):
    exclude = ('status', )

