from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
    def clean_Tile(self):
        data=self.cleaned_data['Tile']
        if len(data)<3 and len(data)>150:
            raise forms.ValidationError('Title must be in 3 to 150 words')
        return data
    def clean_File(self):
        f = self.cleaned_data['File']
        max_length = 5
        if f.size > max_length * 1024 * 1024:
            raise forms.ValidationError(f'File must be in {max_length} mb')
        return f
