from django.forms import ModelForm,TextInput, NumberInput



from .models import Expense


class ExpenseForm(ModelForm):
    class Meta:
        model = Expense

        fields = ['name','category','amount']

        widgets = {
            'name' : TextInput(attrs={
            'class' : "input",
            'id' : "fullname",
            'placeholder' : " "
            }),
            
            'amount' : NumberInput(attrs={
            'class' : "input",
            'id' : "amount",
            'placeholder' : " "
            }),

            'category' : TextInput(attrs={
            'class' : "input",
            'id' : "category",
            'placeholder' : " "
            }),


        }