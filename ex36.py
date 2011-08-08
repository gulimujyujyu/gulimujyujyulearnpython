
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

print 'Use die function!'
useDie = True

def die():
	print 'Dying'
	exit(0)

if useDie:
	die();
else:
	print 'Do not use die.'