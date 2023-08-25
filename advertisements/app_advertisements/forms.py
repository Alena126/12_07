from django.forms import ModelForm, Textarea, TextInput, NumberInput, CheckboxInput, FileInput
from app_advertisements.models import Advertisements
from django.core.exceptions import ValidationError


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ('title', 'description', 'price', 'auction', 'image')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': FileInput(attrs={'class': 'form-control form-control-lg'})
        }

    def clean_title(self):
        title_valid = self.cleaned_data['title']
        if "?" in title_valid[0]:
            raise ValidationError('Заголовок не может начинаться с вопросительного знака')
        return title_valid


