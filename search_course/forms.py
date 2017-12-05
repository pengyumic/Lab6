from django.forms import Select
from django import forms
from .models import Courses

class CoursesForm(forms.ModelForm):
    # email = forms.EmailField(error_messages={'requir'})
    # sel_subj = forms.ChoiceField(choices=subject, error_messages={'required':'Please select a subject'})
    # def clean_sel_subj(self):
    #     subj = self.cleaned_data['sel_subj']
    #     if (subj == '---------'):
    #         raise forms.ValidationError("You have forgotten about subject!")
    #     return subj

    class Meta:
        model = Courses
        fields = [
            'sel_subj', 'sel_crse', 'sel_title', 'sel_schd',
            'sel_insm', 'sel_from_cred', 'sel_to_cred', 'sel_camp',
            'sel_ptrm', 'sel_instr', 'sel_sess', 'sel_attr', 'begin_hh', 'begin_mi',
            'begin_ap', 'end_hh', 'end_mi', 'end_ap', 'sel_day', 'email',
        ]
        widgets = {
            'sel_schd': Select(attrs={'size':'3'}),
            'sel_subj': Select(attrs={'size':'10'}),
            'sel_schd': Select(attrs={'size':'3'}),
            'sel_insm': Select(attrs={'size':'3'}),
            'sel_camp': Select(attrs={'size':'3'}),
            'sel_ptrm': Select(attrs={'size':'3'}),
            'sel_sess': Select(attrs={'size':'3'}),
            'sel_attr': Select(attrs={'size':'3'}),
            'sel_instr': Select(attrs={'size':'3'}),
        }
