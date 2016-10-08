# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Reproduccion
from datetimewidget.widgets import DateTimeWidget

class ReproduccionForm(forms.ModelForm):
    fechaPosibleParto = forms.TextInput()
    class Meta:
        model = Reproduccion

        fields = ['id_bovino', 'id_toro', 'id_servicio', 'id_cria',
                  'id_semen_toro', 'fecha_servicio', 'proximoCelo',
                  'fechaPosibleParto','cantCelosPosParto',
                  'fechaSecado','id_estado']

        labels = {
            'id_bovino': _(u'*Bovino'),
            'id_toro': _(u'Toro'),
            'id_servicio': _(u'*Tipo de servicio'),
            'id_cria': _(u'Identificacion de la cría'),
            'id_semen_toro': _(u'Semen del toro empleado'),
            'fecha_servicio': _(u'*Fecha del servicio'),
            'proximoCelo': _(u'*Fecha del próximo celo'),
            'fechaPosibleParto': _(u'Fecha del posible parto'),
            'fechaSecado': _(u'Fecha del secado'),
            'cantCelosPosParto': _(u'Cantidad de celos posparto'),
            'id_estado': _(u'*Estado de la reproduccion')
        }

        error_messages = {
            'id_bovino': {
                'required': _("El campo del bovino es requerido"),
            },
            'id_servicio': {
                'required': _("El tipo de servicio es requerido"),
            },
            'fecha_servicio': {
                'required': _("La fecha de servicio es requerida"),
            },
            'proximoCelo': {
                'required': _("El proximo celo es requerido"),
            },
            'id_estado': {
                'required': _("La fecha de posible es requerida"),
            }
        }
