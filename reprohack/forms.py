from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Field
from crispy_forms.bootstrap import PrependedText
from reprohack.models import Event, Paper


## -------- Event -------- ##
class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['submission_date', 'user']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit event'))
        self.helper.layout = Layout(
            'title',
            'host',
            Row(
                Column('date', css_class='form-group col-md-4 mb-0'),
                Column('time_start', css_class='form-group col-md-4 mb-0'),
                Column('time_end', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'location',
            'address',
            Row(
                Column('city', css_class='form-group col-md-8 mb-0'),
                Column('postcode', css_class='form-group col-md-4 mb-0'),
            ),
            Row(
                Column('lat', css_class='form-group col-md-6 mb-0'),
                Column('lon', css_class='form-group col-md-6 mb-0'),
            ),
            'registration_url',
        )

    def clean(self):
        authorship = self.cleaned_data.get('authorship')

        if authorship:
            self.cleaned_data['author_user'] = self.user
        else:
            self.cleaned_data['author_user'] = ""
            self.fields_required(['author_first_name'])
            self.fields_required(['author_last_name'])
            self.fields_required(['author_email'])
        return self.cleaned_data
    
    def fields_required(self, fields):
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

## -------- Paper -------- ## 
class PaperForm(ModelForm):
    class Meta:
        model = Paper
        exclude = ['submission_date', 'user', 'author_user']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PaperForm, self).__init__(*args, **kwargs)
        #self.email = self.cleaned_data['email']
        self.fields['authorship'].label = "I am the corresponding author"
        self.fields['contact'].label = "I can be contacted by participants"
        #self.fields['feedback'].label = "I wish to received feedback on reproductions"
        self.fields['public'].label = "I wish to received feedback on reproductions"
        self.helper = FormHelper(self) 
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit event'))
        self.helper.layout = Layout(
            HTML('<h2>Paper details<h2>'),
            'title',
            'citation_txt',
            'citation_bib',
            'doi',
            'description',
            'why',
            'focus',
            Fieldset("Links to Resources",
                Row(
                    Column('paper_url', css_class='form-group col-md-6 mb-0'),
                    Column('data_url',  css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                ),
                Row(
                    Column('code_url', css_class='form-group col-md-6 mb-0'),
                    Column('extra_url', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                ),
            ),
            Field('tools', label = "Useful Software Skills"),
            HTML('<h3>Submitter contact details<h3>'),
            Row(
                Column(PrependedText('twitter', '@', placeholder="twitter username"), css_class='form-group col-md-4 mb-0'),
                Column(PrependedText('github', '@', placeholder="github username"), css_class='form-group col-md-4 mb-0'),
                css_class='form-row',
            ),
            Fieldset("Authorship details",
                Row(
                    Column('authorship', label="I am corresponding author", css_class='form-group col-md-6 mb-0'),
                    Column('author_first_name', css_class='form-group col-md-3 mb-0'),
                    Column('author_last_name',  css_class='form-group col-md-3 mb-0'),
                    Column('author_email',  css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                ),
                Row(
                    Column('public', label="Feedback can be published", css_class='form-group col-md-6 mb-0'),
                    css_class='form-row',
                ),
            ),
        )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #orcid_id = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #affiliation = forms.CharField(max_length=30, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',  'email', 'password1', 'password2')




PrependedText('field_name', '@', placeholder="username")