from FoodApp.models import ReviewModel
from django import forms

class CreateReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields=['rate','text']
        
        widgets = {
            'rate': forms.Select(
				attrs={
					'class': 'form-control'
					}
				),
            'text': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
			}
