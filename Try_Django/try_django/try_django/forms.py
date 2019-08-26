from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    ''' The clean_<fieldname>() method is called on a form subclass – where <fieldname> 
    is replaced with the name of the form field attribute. This method does any cleaning 
    that is specific to that particular attribute, unrelated to the type of field that it is. 
    This method is not passed any parameters. '''
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("This is not a valid email. Please don't use .edu.")
        return email




