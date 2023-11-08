from django import template

register = template.Library()

@register.filter
def get_type(x):
    #return type(x) # <class 'dict'>
    return isinstance(x, dict) # True
    


def pourforloop():
    obj = {
        'nom': 'wali',
        'prenom': 'affi',
        'age': 15,
        'il_a': [
            'telephone',
            'pc',
            'velo',
            'passion de travail'
        ]
    }

    return obj


@register.filter
def addition(x, y):
    return x+y
    
