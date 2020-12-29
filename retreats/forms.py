from django import forms
from products.widgets import CustomClearableFileInput
from .models import Retreat


class RetreatForm(forms.ModelForm):

    class Meta:
        model = Retreat
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, 
            widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ Customize form and form labels """
        super().__init__(*args, **kwargs)
        retreats = Retreat.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
