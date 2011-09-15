
#!/usr/local/bin/python 
# -*- coding:utf-8 -*-
import re

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("One", "Two", "Three", "Four")
print formatter % ('One', 'Two', 'Three', 'Four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said good night."
)

LIGHT_MESSAGES = {
    'English': "There are %(number_of_lights)s lights.",
    'Pirate':  "Arr! Thar be %(number_of_lights)s lights."
}

def lights_message(language, number_of_lights):
    """Return a language-appropriate string reporting the light count."""
    return LIGHT_MESSAGES[language] % locals()

def is_pirate(message):
    """Return True if the given message sounds piratical."""
    return re.search(r"(?i)(arr|avast|yohoho)!", message) is not None

print lights_message('English',12)
print is_pirate("Hello")