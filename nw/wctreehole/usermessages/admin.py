from django.contrib import admin
from .models import Message, Comment
from django.utils.translation import ugettext as _, ugettext_lazy
# Register your models here.

admin.site.register(Message)
admin.site.register(Comment)
admin.site.site_header = ugettext_lazy('Site admin')
admin.site.site_title = ugettext_lazy('Site admin')
