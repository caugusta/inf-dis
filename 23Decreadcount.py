#Written Dec 13th by Carolyn Augusta
#Objective: read in the json file containing dictionaries of counts of infectious individuals at time t.
#For example, epidemic 1: {1:1, 2:6} means at time 1, 1 person became infectious; at time 2, 6 people became infectious

import json
import re
import string
import sys
import numpy as np

#neighbourhood epidemics

#extras

with open( 'epidemics_neighbourhood_Dec23_redo.json', 'r' ) as f :
    data = f.read()

count = len(data.split('}, {')) #should be 800
print 'redo neighbourhood epidemics', count
str_epi = ' '.join(data.split('{'))
str_epi2 = str_epi.split('}')
#print str_epi2[0] #first epidemic

times = re.findall(r'"(.\w*)"', str_epi2[0])
infindivs = re.findall(r':(.\w*),', str_epi2[0]) #need this to also return the last element of the string
lastone = str_epi2[0][-1]
new1 = infindivs
new1.append(lastone)


times = np.asarray(times, dtype=np.int32)
infindivs = np.asarray(infindivs, dtype=np.int32)
newinf = infindivs

i=1
while i < len(str_epi2):
        #print i
        times_1 = re.findall(r'"(.\w*)"', str_epi2[i])
        infindivs_1 = re.findall(r':(.\w*),', str_epi2[i])
        lastone = str_epi2[0][-1]
        newinf = infindivs_1
        newinf.append(lastone)
        if len(newinf) < 2:
                print 'list was empty'
                i += 1
                continue
        else:
                times = np.concatenate((times, np.asarray(times_1, dtype=np.int32)))
                #newinf = np.concatenate((newinf, np.asarray(newinf_1, dtype=np.int32)))
                infindivs = np.concatenate((infindivs, np.asarray(infindivs_1, dtype=np.int32)))
                i += 1


with open('Dec29_neighbourhood_epidemics_redo.txt', 'w') as f:
        np.savetxt(f, np.c_[times, infindivs], fmt=['%i', '%i'])

print 'wrote Dec29_neighbourhood_epidemics_redo.txt'


#original
with open( 'epidemics_neighbourhood_Dec23.json', 'r' ) as f :
    data = f.read()

count = len(data.split('}, {'))
#count = len(data.split('}{')) #should be 8800
print 'original neighbourhood epidemics', count

str_epi = ' '.join(data.split('{'))
str_epi2 = str_epi.split('}')
#print str_epi2[0] #first epidemic

times = re.findall(r'"(.\w*)"', str_epi2[0])
infindivs = re.findall(r':(.\w*),', str_epi2[0]) #need this to also return the last element of the string
lastone = str_epi2[0][-1]
new1 = infindivs
new1.append(lastone)


times = np.asarray(times, dtype=np.int32)
infindivs = np.asarray(infindivs, dtype=np.int32)
newinf = infindivs

i=1
while i < len(str_epi2):
	#print i
	times_1 = re.findall(r'"(.\w*)"', str_epi2[i])
	infindivs_1 = re.findall(r':(.\w*),', str_epi2[i])
	lastone = str_epi2[0][-1]
	newinf = infindivs_1
	newinf.append(lastone)
	if len(newinf) < 2:
		print 'list was empty'
		i += 1
		continue
	else:
		times = np.concatenate((times, np.asarray(times_1, dtype=np.int32)))
		#newinf = np.concatenate((newinf, np.asarray(newinf_1, dtype=np.int32)))
		infindivs = np.concatenate((infindivs, np.asarray(infindivs_1, dtype=np.int32)))
		i += 1
#Now need to export to a file that R can read for plotting epidemics. Want two columns: t and count.
#E.g.:
# t count
# 1  1
# 2  4
# 3  9

with open('Dec29_neighbourhood_epidemics.txt', 'w') as f:
	np.savetxt(f, np.c_[times, infindivs], fmt=['%i', '%i'])

print 'wrote Dec29_neighbourhood_epidemics.txt'


##Exponential

with open( 'epidemics_exponential_Dec23.json', 'r' ) as f :
    data = f.read()

count = len(data.split('}, {'))
#count = len(data.split('}{')) #9600 as desired
print 'exponential epidemics', count

str_epi = ' '.join(data.split('{'))
str_epi2 = str_epi.split('}')
#print str_epi2[0] #first epidemic

times = re.findall(r'"(.\w*)"', str_epi2[0])
infindivs = re.findall(r':(.\w*),', str_epi2[0]) #need this to also return the last element of the string
lastone = str_epi2[0][-1]
new1 = infindivs
new1.append(lastone)


times = np.asarray(times, dtype=np.int32)
infindivs = np.asarray(infindivs, dtype=np.int32)
newinf = infindivs

i=1
while i < len(str_epi2):
        #print i
        times_1 = re.findall(r'"(.\w*)"', str_epi2[i])
        infindivs_1 = re.findall(r':(.\w*),', str_epi2[i])
        lastone = str_epi2[0][-1]
        newinf = infindivs_1
        newinf.append(lastone)
        if len(newinf) < 2:
                print 'list was empty'
                i += 1
                continue
        else:
                times = np.concatenate((times, np.asarray(times_1, dtype=np.int32)))
                infindivs = np.concatenate((infindivs, np.asarray(infindivs_1, dtype=np.int32)))
                i += 1


with open('Dec29_exponential_epidemics.txt', 'w') as f:
        np.savetxt(f, np.c_[times, infindivs], fmt=['%i', '%i'])

print 'wrote Dec29_exponential_epidemics.txt'

##Powerlaw

with open( 'epidemics_powerlaw_Dec23.json', 'r' ) as f :
    data = f.read()

count = len(data.split('}, {'))
#count = len(data.split('}{')) #9600 as desired
print 'powerlaw epidemics', count

str_epi = ' '.join(data.split('{'))
str_epi2 = str_epi.split('}')
#print str_epi2[0] #first epidemic

times = re.findall(r'"(.\w*)"', str_epi2[0])
infindivs = re.findall(r':(.\w*),', str_epi2[0]) #need this to also return the last element of the string
lastone = str_epi2[0][-1]
new1 = infindivs
new1.append(lastone)


times = np.asarray(times, dtype=np.int32)
infindivs = np.asarray(infindivs, dtype=np.int32)
newinf = infindivs

i=1
while i < len(str_epi2):
        #print i
        times_1 = re.findall(r'"(.\w*)"', str_epi2[i])
        infindivs_1 = re.findall(r':(.\w*),', str_epi2[i])
        lastone = str_epi2[0][-1]
        newinf = infindivs_1
        newinf.append(lastone)
        if len(newinf) < 2:
                print 'list was empty'
                i += 1
                continue
        else:
                times = np.concatenate((times, np.asarray(times_1, dtype=np.int32)))
                infindivs = np.concatenate((infindivs, np.asarray(infindivs_1, dtype=np.int32)))
                i += 1


with open('Dec29_powerlaw_epidemics.txt', 'w') as f:
        np.savetxt(f, np.c_[times, infindivs], fmt=['%i', '%i'])

print 'wrote Dec29_powerlaw_epidemics.txt'
