from django import forms

class ContatoForm(forms.Form):
    Nome = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo!', 'class':'padding paddingH'}))
    Email = forms.EmailField(help_text="Um endereço de email válido: exemplo@exemplo.com",widget=forms.TextInput(attrs={'placeholder': 'Um email válido!', 'class':'padding paddingH'}))
    Telefone = forms.CharField(max_length=13,widget=forms.TextInput(attrs={'placeholder': '(54)9xxxxxxx', 'class':'padding paddingH' }))
    Comentarios = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder': 'Dicas, sugestões, currículos, fique a vontade!',  'class':'padding paddingH'}))


