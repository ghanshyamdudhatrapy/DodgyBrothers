from django import forms
from .models import Cars
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
# creating a form
class CarsForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    # password = PasswordField(label="Password")
    # password_confirm = PasswordField(label="Password")
    # create meta class
    class Meta:
        # specify model to be used
        model = Cars
        # specify fields to be used
        fields = [
            "seller_name",
            "seller_mob",
            "make",
            "model",
            "year",
            "condition",
            "price"
        ]
        widgets = {
            'year': DateInput(attrs={'type': 'date'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        seller_name = cleaned_data.get("seller_name")
        seller_mob = cleaned_data.get("seller_mob")
        make = cleaned_data.get("make")
        model = cleaned_data.get("model")
        year = cleaned_data.get("year")
        condition = cleaned_data.get("condition")
        price = cleaned_data.get("price")

        if not seller_name or not seller_mob or not make or not model or not year or not condition or not price:
            # Only do something if both fields are valid so far.

            raise ValidationError(
                "Form has missing details"
            )
