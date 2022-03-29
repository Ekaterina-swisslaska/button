from django import forms


class GoodForm(forms.Form):
    name_good = forms.CharField(label='Наименование товара', max_length=255)
    price = forms.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    size = forms.IntegerField(label="Размер")
    color = forms.IntegerField(label="Цвет")
    description = forms.CharField(label="Описание", widget=forms.Textarea)


class EditGoodDescriptionForm(forms.Form):
   description = forms.CharField(label="Description", widget=forms.Textarea)


class ReviewForm(forms.Form):
    text = forms.CharField(label="Text", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)