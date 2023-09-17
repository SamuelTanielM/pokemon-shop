from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    # Define a list of choices for the "name" field
    NAME_CHOICES = [
        ('MewTwo', 'MewTwo'),
        ('Starmie', 'Starmie'),
        ('Eevee', 'Eevee'),
        ('Suicune', 'Suicune'),
        ('Sceptile', 'Sceptile'),
        ('Haunter', 'Haunter'),
        ('Samurott', 'Samurott'),
        ('Mimikyu', 'Mimikyu'),
        # Add more choices as needed
    ]

    # Create a ChoiceField for the "name" field with the predefined choices
    name = forms.ChoiceField(choices=NAME_CHOICES)

    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
    
    def clean_amount(self):
        name = self.cleaned_data.get('name')
        amount = self.cleaned_data.get('amount')

        # Define the allowable ranges based on the selected name
        allowable_ranges = {
            'MewTwo': (1, 1),
            'Starmie': (1, 100000),
            'Eevee': (1, 100000),
            'Suicune': (1, 10000),
            'Sceptile': (1, 100000),
            'Haunter': (1, 100000),
            'Samurott': (1, 50000),
            'Mimikyu': (1, 100000),
            # Define ranges for other names here
        }

        # Check if the selected name is in the allowable_ranges dictionary
        if name in allowable_ranges:
            min_amount, max_amount = allowable_ranges[name]
            if not min_amount <= amount <= max_amount:
                raise forms.ValidationError(f"The amount for {name} must be between {min_amount} and {max_amount}!")
        
        return amount