from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Search Your City', 'aria-label':'Search', 'aria-describedby': 'search-addon'}))
