from django.contrib import admin
# from django.contrib.auth import admin as 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import (
	UserCreationForm,
	UserChangeForm
)
from .models import (
	User,
	Team,
	Participant
)
# Register your models here.


class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display= ('username','email')
	list_filter = ('is_active',)
	fieldsets = (
		(None,{'fields':('username','email', 'password')}),
		('Permissions', {'fields':('admin','staff')}),
	)
	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('username','email','password1','password2',)
			}
		),
	)

	search_fields = ('username','email',)
	ordering = ('username',)
	filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Participant)
admin.site.register(Team)

