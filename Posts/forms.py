from django import forms

from .models import Posts
from .validators import validate_category

class PostsCreateForm(forms.ModelForm):
    category = forms.CharField(validators=[validate_category])
    email = forms.EmailField()
    class Meta:
        model = Posts
        fields = [
        'name', 'location', 'category', 'text'
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
