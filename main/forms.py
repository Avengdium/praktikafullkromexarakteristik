from dataclasses import fields
from .models import Subs, Products
from django.forms import ModelForm, TextInput, URLInput, EmailInput


class SubForm(ModelForm):
    class Meta:
        model = Subs
        fields = ['MAIL'] 

        widgets = {
            "MAIL": EmailInput(attrs={
                "class": "newsletter_input",
            })
        }

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['ID_PRODUCT', 'NAME_PRODUCT', 'PRICE_PRODUCT', 'IMG_PRODUCT', 'EKRAN_PRODUCT', 'KAMERA_PRODUCT', 'DINAMIK_PRODUCT', 'GODVIPUSKA_PRODUCT'] 

        widgets = {
            "ID_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "ИД продукта"
            }), 

            "NAME_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя продукта"
            }), 

            "PRICE_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Цена продукта"
            }),

            "IMG_PRODUCT": URLInput(attrs={
                "class": "form-control",
                "placeholder": "Введите ссылку на изображение (Обязательно URL картинки!)"

             }),

                "EKRAN_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите разрешение экрана"
            }),

                "KAMERA_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите качество камеры"
            }),

                "DINAMIK_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите тип динамика"
            }),

                "GODVIPUSKA_PRODUCT": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите год выпуска"
            }),
        }