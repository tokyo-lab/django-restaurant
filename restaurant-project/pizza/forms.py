from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust"]


# class PizzaForm(forms.Form):
#     size = forms.ChoiceField(
#         label="Size",
#         choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
#     )
#     crust = forms.ChoiceField(
#         label="Crust",
#         choices=[("regular", "Regular"), ("thin", "Thin")],
#     )
