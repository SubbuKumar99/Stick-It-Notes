from django import forms



class UserContentForm(forms.Form):
    colour_choices = ((1,'Yellow'),(2,'Green'),(3,'Purple'),(4,'Blue'),(5,'Orange'))

    user_author = forms.CharField(label='Author',max_length=20)
    user_title = forms.CharField(label='Title',max_length=50)
    user_content = forms.CharField(label='Content',max_length=150)
    user_colour = forms.ChoiceField(choices=colour_choices,label='Colour')
