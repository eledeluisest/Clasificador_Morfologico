"""
Generación de unamorfología a partir de un texto
Dependencias:
import nltk
nltk.download('punkt')

Etiquetas:
1. Advervios: ADV
2. Artículos:ART
3. Adjetivos:ADJ
4. Determinantes: DET
5. Pronombres: PRON
6. Conjunciones: CONJ
7. Numerales: NUM
8. Interjecciones: INT
9. Abreviaturas:ABRV
10. Preposiciones: PREP
11. Signos de puntuación: PUNT

Verbos y nombres:
http://www.cs.upc.edu/~nlp/tools/parole sp.html
Utilizamos genero, numero y tipo para nombres
"""
#!/usr/bin/env python
# -*- coding: utf 8  -*-
import sys
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from importlib import reload
reload(sys)
#sys.setdefaultencoding('utf8')
#Lectura del fichero de texto
f = open ('data/texto.txt')
freqdist = nltk.FreqDist()
words=nltk.word_tokenize(f.read())
fd = nltk.FreqDist(word.lower() for word in words)
fdf= fd.most_common(50)

print('Palabras del texto ordenadas por frecuencia')
print('Palabras del texto ordenadas por frecuencia')

t=''
t=''
for w in fdf:
    t += '(' + w[0] + ',' + str(w[1]) + ') '
print(t)

dict ={}

# Aquí hay se añaden las palabras del diccionario y sus etiquetas
# Lo utilizaremos para palabras concretas
dict['.']='PUNT'
dict['la']='DET'
dict['a']='PREP'
dict['para']='PREP'
dict['que']='CONJ'
dict['en']='PREP'
dict['el']='DET'
# INCLUIMOS DE LAS PALABRAS MUY REPETIDAS
dict['de']='PREP'
dict['y']='CONJ'
dict['los']='DET'
dict['las']='DET'
dict['del']='DET'
dict[','] = 'PUNT'
dict['para'] = 'PREP'
dict['un']='DET'
dict['una']='DET'
dict['es'] = 'VMIP3S'
dict['son'] = 'VMIP3S'
dict['con'] = 'PREP'
dict['su'] = 'DET'
dict['o'] = 'CONJ'
dict['hacia'] = 'PREP'
dict['por'] = 'PREP'
dict['no'] = 'ADV'
dict[':'] = 'PUNT'
dict['lo'] = 'PRON'
dict['cuando'] = 'ADV'


# Excepciones que metemos a las terminaciones de palabras que son en si mismas palabras con sentido.
dict['antes'] = 'ADV'
dict['mente'] = 'NCFS'
dict['ante'] = 'PREP'

"""
Palabras en duda: se, al, como,  
forma,
"""

# Estas palabras dan problema por los caracteres especiales
dict['tambiã©n'] = 'ADV'
dict['mã¡s'] = 'ADV'
dict['deberã¡n'] = 'VAIF3P'


# Aquí hay se añaden los patrones necesarios#Aquí hay se añaden los patrones necesarios
# Reglas generales

p=[
(r'.*amos$','VIP1S'),
(r'.*emos$','VIP1S'),
(r'.*imos$','VIP1S'),

(r'.*illa$','NCFS'),
(r'.*illo$','NCMS'),
(r'.*illas$','NCFP'),
(r'.*illos$','NCMP'),

(r'.*ar$','VMN'),
(r'.*er$','VMN'),
(r'.*ir$','VMN'),

(r'.*mente$','ADV'),

(r'.*or$','NCMS'),
(r'.*ora$','NCFS'),
(r'.*ores$','NCMP'),
(r'.*oras$','NCFP'),

(r'.*ores$','NCMP'),
(r'.*oras$','NCFP'),

(r'.*al$','ADJ'),
(r'.*ales$','ADJ'),

(r'.*ad$','NCFS'),
(r'.*ades$','NCFP'),


(r'.*ion$','NCMS'),
(r'.*iones$','NCMS'),

(r'.*[0-9]$','NUM'),

(r'.*as$','NCFP'),
(r'.*a$','NCFS'),
(r'.*$','NCMS')

]
rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)

# Guardamos la información de los items y sus clasificaciones para después poder cruzar con las repeticiones
resultado = {}
for item in taggedText:
    if item[0] in dict:
        print (item[0]+' '+dict[item[0]])
        resultado[item[0]] = dict[item[0]]
    else:
        print (item[0]+' '+item[1])
        resultado[item[0]] = item[1]

with open('data/top50.csv','w+') as f:
    for palabra, frecuencia in fdf:
        try:
            f.writelines(';'.join([palabra,str(frecuencia),resultado[palabra]])+'\n')
        except:
            print(palabra)



