from ipaddress import *
import statistics as stat
from copy import deepcopy
import json 
from rich import print

def calcul():
    
    asPass = []

    for line in open('ris.json','r'):
        try:
            tmp = len(json.loads(line)['data']['path'])
            if tmp !=0:
                asPass.append(deepcopy(tmp))
            

        except KeyError:
            continue

    asPass.sort()
    if len(asPass)%2==0:
        med = asPass[len(asPass)//2]
    else:
        med = asPass[len(asPass)//2] + asPass[len(asPass)//2] - asPass[len(asPass)//2-1]
    print(f'moyenne d AS traversée : {round(stat.mean(asPass),2)}\nMédianne d AS traversée : {med}')

#calcul()


def pourcentage46():

    ipv4,ipv6=[],[]

    for line in open('ris.json','r'):

        ipv=ip_network(json.loads(line)['data']['peer'])

        if isinstance(ipv,IPv4Network):
            ipv4.append(ipv4)
        else:
            ipv6.append(ipv4)
    print(f"il y a {round(len(ipv4)*100/(len(ipv4)+len(ipv6)),2)}% d'ipv4 et {round(100-len(ipv4)*100/(len(ipv4)+len(ipv6)),2)}% d'ipv6")


import pandas as pd
pd.set_option('display.expand_frame_repr', False)

listeAction = []
listePref = []
listeASorig = []
listeASpath = []
listeLenPath = []
ok = True
for line in open('ris.json','r'):
    try:
        listePref.append(json.loads(line)['data']['announcements'][0]['prefixes'])

        listeASorig.append(json.loads(line)['data']['path'][len(json.loads(line)['data']['path'])-1])
    
        listeASpath.append(json.loads(line)['data']['path'])
        listeLenPath.append(len(json.loads(line)['data']['path']))
    except KeyError:
            continue
    
    listeAction.append(json.loads(line)['data']['type'])


#print(len(listeAction),len(listePref),len(listeASorig),len(listeASpath),len(listeLenPath))
data = {'Action':listeAction,'Préfixes':listePref,'AS_origine':listeASorig,'ASpath':listeASpath,'lenPath':listeLenPath}
# création du dataframe df
df = pd.DataFrame(data)
# Affichage
print(df)


pourcentage46()