from django import forms


class PizzaForm(forms.Form):
    size = forms.ChoiceField(
        label="Size",
        choices=[("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")],
    )
    crust = forms.ChoiceField(
        label="Crust",
        choices=[("Regular", "Regular"), ("Thin", "Thin")],
    )
