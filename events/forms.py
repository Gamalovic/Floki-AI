from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'formInput', 'id': 'eventName'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'formInput', 'id': 'aboutEvent', 'style': 'resize:none'}))
    date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'formInput', 'id': 'datepicker', 'type': 'date'}))
    year = forms.IntegerField(max_value=4, min_value=1, widget=forms.NumberInput(
        attrs={'class': 'formInput', 'id': 'gradePicker', 'type': 'number'}))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'name': 'file', 'id': 'file'}))
    # image = forms.FileField(widget=forms.FileInput(
    #    attrs={'name': 'file', 'id': 'file'}))

    class Meta:
        model = Event
        fields = ('name', 'description', 'date', 'year', 'image')

    def save(self, commit=True):
        event = super(EventForm, self).save(commit=False)
        event.name = self.cleaned_data['name']
        event.description = self.cleaned_data['description']
        event.date = self.cleaned_data['date']
        event.year = self.cleaned_data['year']
        event.image = self.cleaned_data['image']

        if commit:
            event.save()

        return event
