from django import forms
import json


class RpcCallForm(forms.Form):
    method = forms.CharField(label="Method", max_length=100)
    params = forms.CharField(
        label="Params (JSON)", required=False, widget=forms.Textarea(attrs={"rows": 3})
    )

    def clean_params(self):
        params = self.cleaned_data.get("params")
        if params:
            try:
                return json.loads(params)
            except json.JSONDecodeError:
                raise forms.ValidationError("Invalid JSON format")
        return {}
