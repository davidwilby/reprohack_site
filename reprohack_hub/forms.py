import json
from typing import Any, Optional, Dict, Union, Type, Sequence

from django.forms import Field as DFField, ModelForm, Widget, TextInput, RadioSelect, CharField
from django.forms.models import ModelChoiceField
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column, HTML, Field
from crispy_forms.bootstrap import InlineRadios
# from leaflet.forms.widgets import LeafletWidget

from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError

from .models import Event, Paper, Review, PaperReviewer


# -------- Event -------- #
class MapInput(Widget):
    template_name = "event/map_input_widget.html"



class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['submission_date', 'creator']
        widgets = {'event_coordinates': MapInput()}

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit event'))
        self.helper.layout = Layout(
            'title',
            'host',
            Row(
                Column('start_time', css_class='form-group col-md-4 mb-0'),
                Column('end_time', css_class='form-group col-md-4 mb-0'),
                Column('time_zone', css_class='form-group col-md-4 mb-0'),
                css_class='form-row',
            ),
            # 'venue',
            'description',
            'address1',
            'address2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('postcode', css_class='form-group col-md-3 mb-0'),
                Column('country', css_class='form-group col-md-3 mb-0'),
            ),
            'registration_url',
            'event_coordinates',
        )


# -------- Paper -------- #
class PaperForm(ModelForm):
    class Meta:
        model = Paper
        exclude = ['submission_date', 'creator', ]
        widgets = {
            'title': TextInput(),
            'review_availability': RadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        super(PaperForm, self).__init__(*args, **kwargs)
        # self.email = self.cleaned_data['email']

        # self.fields['authorship'].label = "I am the corresponding author"
        # self.fields['contact'].label = "I can be contacted by participants"

        # self.fields['feedback'].label = "I wish to received feedback on reproductions"

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit paper'))
        self.helper.layout = Layout(
            HTML('<h2>Paper details<h2>'),
            'event',
            'title',
            'authors',

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
            Field('tools', label="Useful Software Skills"),
            Fieldset("Permissions",
                     "review_availability",
                     "public_reviews",
                     "email_review")
        )


class MuWidget(Widget):

    template_name = "review/reviewers_select.html"

    def get_context(self, name: str, value: Any, attrs):
        context = super().get_context(name, value, attrs)
        context["user"] = self.user
        return context


class MuField(DFField):
    instance = None
    widget = MuWidget

    def clean(self, value):
        return value

class ReviewForm(ModelForm):

    """A form to review papers.

    Todo:
        * Test the query of available papers with respect to event.
    """

    reviewers = MuField()

    class Meta:
        model = Review
        exclude = ['reviewers']


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["reviewers"].widget.user = self.user
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit review'))
        self.helper.layout = Layout(
            # HTML('<h2>ReproHack Author Feedback Form</h2>'),
            'reviewers',
            'event',
            'paper',
            HTML(f"<h3>{_('Reproducibility')}</h3>"),
            'reproducibility_outcome',
            InlineRadios('reproducibility_rating'),
            'reproducibility_description',
            'familiarity_with_method',
            Fieldset(_("Operating System"),
                     Row(
                         Column('operating_system',
                                css_class='form-group col-md-4 mb-0'),
                         Column('operating_system_detail',
                                css_class='form-group col-md-8 mb-0')
            )),
            'software_installed',
            'software_used',
            'challenges',
            'advantages',
            'comments_and_suggestions',
            HTML('<h3>Documentation</h3>'),
            InlineRadios('documentation_rating'),
            'documentation_cons',
            'documentation_pros',
            InlineRadios('method_familiarity_rating'),
            'transparency_suggestions',
            HTML(f"<h3>{_('Reusability')}</h3>"),
            InlineRadios('method_reusability_rating'),
            Fieldset(_("Are materials clearly covered by a "
                       "permissive enough license to build on?"),
                     Row(
                         Column('data_permissive_license',
                                css_class='form-group col-md-6 mb-0'),
                         Column('code_permissive_license',
                                css_class='form-group col-md-6 mb-0'),
            )),
            'reusability_suggestions',
            'general_comments',
            Fieldset(_("Permissions"),
                     "public_review"
                     )
        )

    def clean(self) -> Dict[str, Any]:
        # user = self.user
        # raise ValidationError(f"Test returning error message", code='invalid')
        return super().clean()

    def save(self, commit: bool = ...) -> Any:
        save_result = super().save(commit)
        review = self.instance

        reviewers_data_str = self.cleaned_data["reviewers"]
        reviewers_data = json.loads(reviewers_data_str)

        review.reviewers.clear()
        for reviewer_obj in reviewers_data:
            user = get_user_model().objects.get(username=reviewer_obj["username"])
            review.reviewers.add(user, through_defaults={"lead_reviewer": reviewer_obj["lead"]})
        review.save()

        return save_result





# --------------- USER PROFILE ---------------------- #


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = get_user_model()
        exclude = ["password", "id_password"]
        fields = ['name', 'email', 'bio', 'affiliation', 'location', 'twitter', 'github', 'orcid']

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        fields = ('first_name', "last_name", 'username', 'email', 'password1', 'password2', 'affiliation', 'twitter', 'github', 'orcid')
        model = get_user_model()

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Sign up'))
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-5 mb-0'),
                Column('last_name', css_class='form-group col-md-7 mb-0')
            ),
            'username',
            'email',
            Row(
                Column('password1', css_class='form-group col-md-6 mb-0'),
                Column('password2', css_class='form-group col-md-6 mb-0')
            ),
            'affiliation', 'twitter', 'github', 'orcid',

        )
