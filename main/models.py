from django.db import models
from django.core.exceptions import ValidationError

#Валидация ДНК

def validate_DNA(value) :
    value.lower()
    for nucleotide in value :
        if nucleotide != 'a' and nucleotide != 'c' and nucleotide != 'g' and nucleotide != 't' :
            print(nucleotide)
            raise ValidationError("Incorrect nucleotide in DNA")
    return value

class DNA(models.Model) :
    chain = models.CharField(max_length=200,
                             validators=[validate_DNA])

