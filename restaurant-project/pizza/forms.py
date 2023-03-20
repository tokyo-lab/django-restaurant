from django import forms

from .models import Pizza, Customer


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust", "addons"]
        labels = {""}
        widgets = {
            "size": forms.RadioSelect,
            "crust": forms.RadioSelect,
            "addons": forms.CheckboxSelectMultiple,
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email"]


# class PizzaForm(forms.Form):
#     size = forms.ChoiceField(
#         label="Size",
#         choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
#         widget=forms.RadioSelect,
#     )
#     crust = forms.ChoiceField(
#         label="Crust",
#         choices=[("regular", "Regular"), ("thin", "Thin")],
#         widget=forms.RadioSelect,
#     )

#     addons = forms.MultipleChoiceField(
#         label="Addons",
#         choices=[("pepperoni", "Pepperoni"), ("ham", "Ham")],
#         widget=forms.CheckboxSelectMultiple,
#     )


# class CustomerForm(forms.Form):
#     name = forms.CharField(
#         label="name",
#         max_length=100,
#     )
#     email = forms.EmailField(label="email", max_length=100)
