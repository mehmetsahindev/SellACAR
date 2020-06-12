from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, forms, ModelForm, Select, FileInput

from home.models import UserProfile
from product.models import Product


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'email': EmailInput(attrs={'placeholder': 'email'}),
            'first_name': TextInput(attrs={'placeholder': 'first name'}),
            'last_name': TextInput(attrs={'placeholder': 'last name'}),
        }


CITY = [
    ('Istanbul', 'Istanbul'),
    ('Karabük', 'Karabük'),
    ('Hatay', 'Hatay'),
]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'city': Select(attrs={'placeholder': 'city'}, choices=CITY)
        }


class UserProductForm(ModelForm):
    class Meta:
        model = Product
        fields = (
        'category', 'title', 'keywords', 'description', 'image', 'marka', 'model', 'renk', 'year', 'kilometre', 'vites',
        'durum', 'price', 'amount', 'detail', 'slug')
        widgets = {
            'image': FileInput(),
            'detail': CKEditorWidget(),
        }
