from django import forms

from sportapp.models import Supplement


class SupplementForm(forms.ModelForm):
    class Meta:
        model = Supplement
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(SupplementForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
