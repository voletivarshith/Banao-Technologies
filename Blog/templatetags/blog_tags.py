from django import template

register = template.Library()
@register.filter(name="split")
def split_and_divide(string,count):
    string = string.split()
    if len(string)>15:
        return ' '.join(string[:count])+"..."
    else:
        return ' '.join(string)

@register.filter(name="str")
def tostring(string):
    return str(string)