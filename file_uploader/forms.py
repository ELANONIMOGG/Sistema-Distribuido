from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(
        label='Seleccionar archivo',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '*/*'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({
            'class': 'form-control',
            'id': 'file-input'
        })