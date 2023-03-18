from django import forms


class PizzaForm(forms.Form):
    size = forms.ChoiceField(
        label="Size",
        choices=[("small", "Small"), ("medium", "Medium"), ("large", "Large")],
    )
    crust = forms.ChoiceField(
        label="Crust",
        choices=[("regular", "Regular"), ("thin", "Thin")],
    )
