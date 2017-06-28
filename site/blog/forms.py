from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = (
			"user",
			"title",
			"content",
			"link_to_image"

		)


# #new_today
# class ComForm(forms.ModelForm):
# 	class Meta:
# 		model=Comment
# 		fields=('text',)

# def save(self, user, post):
# 	obj=super(ComForm, self).save(commit=False)
# 	obj.user=user
# 	obj.post=str(post)
# 		return obj.save()		