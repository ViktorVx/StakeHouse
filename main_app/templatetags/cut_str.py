
from django import template
#import regex as re

register = template.Library()



def cut_str(value, arg):
	#result = re.search(r'\w' + '{' + str(arg) + '}', value)
	return 'sss '+ value + '...'
	
	
register.filter('cut_str', cut_str)