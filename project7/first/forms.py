from django import forms
from first.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Studnet Roll'
        }
        