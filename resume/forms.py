from django import forms
from resume.models import Resume

GENDER=[
    ('Male','Male'),
    ('FeMale','FeMale'),
]
LANGUAGES=[
    ('Hindi','Hindi'),
    ('English','English'),
    ('Other','Other'),
]
class resumeform(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER,widget=forms.RadioSelect())
    language = forms.MultipleChoiceField(choices=LANGUAGES,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields= ('id','name','email','dob','gender','language','pincode','state','city','photo','doc')
        labels={'name':'Full_Name','email':'Email','dob':'Date_of_Birth','photo':'Upload_Pic: ','doc':'Upload_resume: '}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
           
        }