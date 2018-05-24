#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: re

# Copyright (C) 2018 liyunteng
# Last-Updated: <2018/05/18 15:57:27 liyunteng>
import re

# match
m = re.match('foo', 'foo')
if m is not None:
    print(m.group())
m = re.match('foo', 'food on the table')
if m is not None:
    print(m.group())

# search
m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())

# |
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

m = re.match(bt, 'blt')         # can't match
if m is not None:
    print(m.group())

m = re.match(bt, 'He bit me!')  # can't match
if m is not None:
    print(m.group())

m = re.search(bt, 'He bit me!')
if m is not None:
    print(m.group())

#.
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print(m.group())

m = re.match(anyend, 'end')     # can't match
if m is not None:
    print(m.group())

m = re.match(anyend, '\nend')   # can't match \n
if m is not None:
    print(m.group())

m = re.search('.end', 'The end.')
if m is not None:
    print(m.group())


patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt, '3.14')
if m is not None:
    print(m.group())

m = re.match(patt314, '3014')
if m is not None:
    print(m.group())

m = re.match(patt314, '3.14')
if m is not None:
    print(m.group())


# []
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print(m.group())

m = re.match('[cr][23][dp][o2]', 'c2do')
if m is not None:
    print(m.group())

m = re.match('r2d2|c3po', 'c2do')  # can't match
if m is not None:
    print(m.group())


#
patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print(m.group(), m.groups())
m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print(m.group(), m.groups())

patt = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt, 'nobody@www.xxx.yyy.zzz.com')
if m is not None:
    print(m.group(), m.groups())

patt = '\w\w\w-\d\d\d'
m = re.match(patt, 'abc-123')
if m is not None:
    print(m.group())
m = re.match(patt, 'abc-xyz')   # can't match
if m is not None:
    print(m.group())

patt = '(\w\w\w)-(\d\d\d)'
m = re.match(patt, 'abc-123')
if m is not None:
    print(m.group())
    print(m.group(1), m.group(2))
    print(m.groups())

m = re.match('ab', 'ab')
if m is not None:
    print(m.group(), m.groups())  # groups() is empty

m = re.match('(ab)', 'ab')
if m is not None:
    print(m.group(), m.groups())  # groups() is not empty

m = re.match('(a)(b)', 'ab')
if m is not None:
    print(m.group(), m.groups())

m = re.match('(a(b))', 'ab')
if m is not None:
    print(m.group(), m.groups())  # groups() have two

# bound
patt = '^The'
m = re.search(patt, 'The end.')
if m is not None:
    print(m.group())
m = re.search(patt, 'end. The')     # can't match
if m is not None:
    print(m.group())

patt = r'\bthe'
m = re.search(patt, 'bitethe dog')  # can't match
if m is not None:
    print(m.group())
m = re.search(patt, 'bite the dog')
if m is not None:
    print(m.group())

patt = r'\Bthe'
m = re.search(patt, 'bitethe dog')
if m is not None:
    print(m.group())


# findall
patt = 'car'
m = re.findall(patt, 'car')
if len(m) > 0:
    print(m)

m = re.findall(patt, 'scary')
if len(m) > 0:
    print(m)

m = re.findall(patt, 'carry the barcardi to the car')
if len(m) > 0:
    print(m)

s = 'This and that.'
patt = '(th\w+) and (th\w+)'
m = re.findall(patt, s, re.I)
print(m)
it = re.finditer(patt, s, re.I)
for x in it:
    print(x.groups())

it = re.finditer(r'(th\w+)', s, re.I)
for x in it:
    print(x.groups())

[g.group() for g in re.finditer(r'(th\w+)', s, re.I)]


# sub
m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print(m)
m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n')
print(m)

m = re.sub('[ae]', 'X', 'abcdef')
print(m)

m = re.subn('[ae]', 'X', 'abcdef')
print(m)

m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',  # 2/20/91 --> 20/2/91
           r'\2/\1/\3', '2/20/91')
print(m)
m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',
           r'\2/\1/\3', '2/20/1991')
print(m)

# split
m = re.split(':', 'str1:str2:str3')
print(m)

DATA = (
    'Mountain View, CA 94040',
    'Sunnyvale, CA',
    'Los Altos, 94023',
    'Cupertino 95014',
    'Palo Alto CA',)
for datum in DATA:
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))


# extra
m = re.findall('(?i)yes', 'yes?Yes, YES!!')  # (?i)=re.I/IGNORECASE
print(m)
m = re.findall('(?i)th\w+', 'The quickest way is through this tunnel.')
print(m)

s = """
This line is the first
another line
that line is't the best
"""
m = re.findall(r'(?im)(^th[\w ]+)', s)  # (?m)=re.M/MULTILINE
print(m)

m = re.findall(r'th.+', s)
print(m)
m = re.findall(r'(?s)th.+', s)  # (?s)=re.S/DOTALL
print(m)


m = re.search(r'''(?x)          # (?x)=re.X/VERBOSE
\((\d{3})\)
[ ]
(\d{3})
-
(\d{4})
''', '(800) 555-1212')
print(m.groups())

m = re.findall(r'http://(?:\w+\.)*(\w+\.com)',
               'http://google.com http://www.google.com http://code.google.com')
print(m)

m = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
              '(800) 555-1212')
print(m.groupdict())

m = re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
           '\g<areacode> \g<prefix>-xxxx', '(800) 555-1212')
print(m)


m = re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)',
             '(800) 555-1212 800-555-1212 18005551212')
print(m.groups())


m = re.match(r'''(?x)
# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

# space
[ ]

# match 800-555-1212
(?P=areacode)-(?P=prefix)-(?P=number)

# space
[ ]

# match 18005551212
1(?P=areacode)(?P=prefix)(?P=number)
''', '(800) 555-1212 800-555-1212 18005551212')
print(bool(m))


m = re.findall(r'\w+(?= van Rossum)',  # (?=)
               '''
               Guido van Rossum
               Tim Peters
               Alex Martelli
               Just van Rossum
               Raymond Hettinger''')
print(m)

m = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',  # (?m)
               '''
               sales@phptr.com
               postmaster@phptr.com
               eng@phptr.com
               noreply@phptr.com
               admin@phptr.com''')
print(m)

m = ['%s@aw.com' % e.group(1) for e in \
 re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
             '''
             sales@phptr.com
             postmaster@phptr.com
             eng@phptr.com
             noreply@phptr.com
             admin@phptr.com''')]
print(m)

print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))


# others
m = re.match('\bblow', 'blow')  # can't match
if m:
    print(m.group())

m = re.match('\\bblow', 'blow')
if m:
    print(m.group())

m = re.match(r'\bblow', 'blow')
if m:
    print(m.group())


import os
m = os.popen('who').read()
re.split(r'\s\s+', m)

#
data = 'Tue Jan 13 05:54:13 1970::ineez@wzenkdcqdm.gov::1029253-5-10'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt, data)
print(m.group(), m.groups())


patt = '^(\w{3})'
m = re.match(patt, data)
if m is not None:
    print('##')
    print(m.group(), m.groups())


#
patt = '\d+-\d+-\d+'
m = re.search(patt, data)
print(m.group())

patt = '.+\d-\d+-\d+'
m = re.search(patt, data)
print(m.group())

patt = '.+(\d+-\d+-\d+)'
m = re.search(patt, data)
print(m.group(1))

patt = '.+?(\d+-\d+-\d+)'       # ? to change greedy
m = re.search(patt, data)
print(m.group(1))

patt = '-(\d+)-'
m = re.search(patt, data)
print(m.group(1))
