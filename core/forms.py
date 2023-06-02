from captcha.fields import CaptchaField
from django.forms import ModelForm
from core.models import *
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class FormCliente(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Cliente
        fields = '__all__'


class FormVeiculo(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Veiculo
        fields = '__all__'


class FormMarca(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Marca
        fields = '__all__'


class FormRotativo(ModelForm):
    #captcha = CaptchaField()

    class Meta:
        model = Rotativo
        fields = '__all__'
        widgets = {'entrada':DateTimePickerInput(), 'data_saida': DateTimePickerInput()}


class FormTabela(ModelForm):
    class Meta:
        model = Tabela
        fields = "__all__"


class FormMensalista(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'
