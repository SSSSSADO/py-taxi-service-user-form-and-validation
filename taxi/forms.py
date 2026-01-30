import re

from django import forms

from taxi.models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    password = None

    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        if not license_number:
            raise forms.ValidationError(
                "Enter license number."
            )
        if len(license_number) != 8:
            raise forms.ValidationError(
                "The license number must contain exactly 8 characters."
            )
        if not re.match(r"^[A-Z]{3}\d{5}$", license_number):
            raise forms.ValidationError(
                "The license must begin with 3 capital letters "
                "and end with 5 numbers."
            )
        return license_number


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
        widgets = {
            "drivers": forms.CheckboxSelectMultiple()
        }
