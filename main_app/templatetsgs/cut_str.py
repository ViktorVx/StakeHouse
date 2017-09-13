
from django import template
import regex as re

register = template.Library()
register.filter('cut_str', cut_str)

@register.filter(name='cut_str')
def cut_str(value, arg):
	result = re.search(r'\w' + '{' + str(arg) + '}', value)
	return result.group(0) + '...'