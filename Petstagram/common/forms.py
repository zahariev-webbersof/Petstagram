from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            },
        ),
    )

# from Petstagram.common.models import Comment
# from Petstagram.pets.models import Pet
#
#
# class CommentForm(forms.ModelForm):
#     pet_id = forms.IntegerField(
#         widget=forms.HiddenInput()
#     )
#
#     class Meta:
#         model = Comment
#         fields = ('text', 'pet_id')
#
#     def save(self, commit=True):
#         pet_pk = self.cleaned_data['pet_pk']
#         pet = Pet.objects.get(pk=pet_pk)
#         comment = Comment(
#             text=self.cleaned_data['text'],
#             pet=pet,
#         )
#         if commit:
#             comment.save()
#
#         return comment
