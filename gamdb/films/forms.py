from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

class CommentForm(forms.Form):
    author = forms.CharField(required=False)
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5,"class=":"form-control"}))#dela z mensiho policka textfield(vytvori widget),rows ja velky
    rating = forms.IntegerField(required=False,
    validator=[MinValueValidator(1),MaxValueValidator(5)])#validator pro data