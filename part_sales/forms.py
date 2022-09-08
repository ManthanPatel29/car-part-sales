# from django import forms
# from .models import part_info
# class part_info(forms.Form):
#     name = forms.CharField(label='Part Name', max_length=100)
#     car_name = forms.CharField(label='Car name/Model No', max_length=100)
#     brand_name = forms.CharField(label='Car Brand', max_length=100)
#     category = forms.CharField(label='Category', max_length=100)
#     desc = forms.CharField(label='Description', max_length=100, widget=forms.Textarea)
#     is_new = forms.BooleanField()
# class part_info_form(forms.ModelForm):
#     class Meta:
#         model = part_info
#         fields = ('name', 'car_name', 'brand_name', 'category', 'description', 'is_new')