from django.contrib import admin
from django import forms
from core.models import *

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project

# TODO Imparare a gestire i campi con valori multipli pilotati
class TransactionForm(forms.ModelForm):
    type = forms.ChoiceField(choices=Transaction.TYPE)


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    form = TransactionForm


admin.site.register(Project, ProjectAdmin)
admin.site.register(Feature)
admin.site.register(Transaction)
admin.site.register(UserDetail)
admin.site.register(Message)