from django import forms
from .models import Pizza
from .models import Customer


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust"]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email"]


# class PizzaForm(forms.Form):
#     size = forms.ChoiceField(
#         label="Size",
#         choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
#     )
#     crust = forms.ChoiceField(
#         label="Crust",
#         choices=[("regular", "Regular"), ("thin", "Thin")],
#     )
