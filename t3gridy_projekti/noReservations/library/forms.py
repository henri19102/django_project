from django import forms

review_choices = (1,2,3,4,5)

class ReviewForm(forms.Form):
    choice_field = forms.ChoiceField()
    text_field = forms.CharField()