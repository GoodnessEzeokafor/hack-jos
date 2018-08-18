# from django import forms
# from .models import Users
# from django.contrib.auth.forms import ReadOnlyPasswordHashField

# class UserCreationForm(forms.Form):
#     """
#     """
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)


#     class Meta:
#         model = Users
#         fields = [
#             'full_name',
#             'username',
#             'email',
#             'team',
#             'startup'
#         ]


    
#     def cleaned_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')

#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Password didn\t match')
#         return password2
    

#     def save(self,commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user



# class UserChangeForm(forms.Form):
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = Users
#         fields = [
#             'full_name',
#             'username',
#             'email',
#             'startup'
#             'password'
#         ]




#     def cleaned_password(self):
#         return self.initial['password']

