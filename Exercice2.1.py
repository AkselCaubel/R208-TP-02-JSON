import json 
from rich import print


def afficheX(x):

    i = 0

    for line in open('ris.json','r'):
        if x == i:
            break
        print(f'"{json.loads(line)["data"]["peer_asn"]}"')
        i+=1



afficheX(int(input("Les X combien vous voulez afficher ? : ")))
