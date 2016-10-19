# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Bovino

class BovinoForm(forms.ModelForm):
    class Meta:
        model = Bovino
        fields = ['id_bovino','id_raza',
        'id_padre','id_madre','id_granja','id_parto',
        'id_procedencia','id_estado','id_etapa',
        'id_sexo','fecha_nacimiento','peso_nacimiento',
        'fecha_destete','edad_primer_parto','fechaEntrada',
        'fechaSalida','motivo_salida','fecha_primer_servicio']

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        cc_myself = cleaned_data.get("cc_myself")
        subject = cleaned_data.get("subject")

        if cc_myself and subject:
            # Only do something if both fields are valid so far.
            if "help" not in subject:
                raise forms.ValidationError(
                    "Did not send for 'help' in the subject despite "
                    "CC'ing yourself."
                )
