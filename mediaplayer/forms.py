from django import forms
from .models import UploadMovie, Comment

class UploadMovieForm(forms.ModelForm):
    class Meta:
        model = UploadMovie
        
        fields = ["title", "thumbnail", "description", "movie" , "name"]
        widgets = {
  

            "title": forms.TextInput(attrs={"class": "form-control","placeholder":"racipe"}),
            "thumbnail": forms.FileInput(attrs={"class": "form-control",}),
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder":"G-mail_Id.."}),
           
            "description": forms.Textarea(attrs={"class": "form-control","placeholder":"Ingredients../process.."}),
            "movie": forms.FileInput(
                attrs={"class": "form-control","accept": "video/*"}
            ),
           
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'comments']
        labels = {
             "full_name": "",
             "comments": "",
         }
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "f_com",'placeholder':"Name.." }),
            "comments": forms.Textarea(attrs={"class": "f_com", 'placeholder':"Comments...." }),
        }

