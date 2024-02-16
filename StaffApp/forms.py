
from django.forms import ModelForm,TextInput
from .models import Product

class ProductAddForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","image","MRP","timester"]
        
        # widgets = {
        #     "expiry_date":TextInput(attrs={"type":'date'}),
        #     "date_of_manufacture":TextInput(attrs={"type":"date"}),
            
        # }
