from django import forms
from django.core import validators

#widgets == field into html input
class contactForm(forms.Form):
    name = forms.CharField(label='User Name :', initial="Your name", help_text="Enter your name", required=False, disabled=False, widget=forms.Textarea(attrs = {'id' : 'textarea','placeholder' : 'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label= "User Email")
    # age = forms.IntegerField() 
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    Agree = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'),('M', 'Medium'),('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    TOPPINGS = [('B','Beef'), ('M', 'Mashroom'), ('P', 'Pepperoni'), ('O', 'Olive')]
    pizza = forms.MultipleChoiceField(choices=TOPPINGS, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name =forms.CharField(widget=forms.TextInput)
#     email =forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email must contain .com")
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email must contain .com")

    # class StudentData(forms.Form):
    #     name =forms.CharField(validators=[validators.MaxLengthValidator(10, message='Enter at least 10 characters')])
    #     email =forms.CharField(widget=forms.EmailInput)
    #     age = forms.CharField()

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")

