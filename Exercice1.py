import subprocess
import jc
cmd_output = subprocess.check_output(['ss', '-tun'],text=True)
data = jc.parse('ss', cmd_output)

f1 = open('content ss -tun.txt','w',encoding='utf-8')


possible = ['ESTAB','LISTENING','FIN-WAIT-1','FIN-WAIT-2','TIME-WAIT','CLOSED','CLOSE-WAIT','SYNC-SEN','SYNC-REC','LAST-AC','CLOSIN']
etats = []
ports = []
addr = []
skip = 0
for dic in data:
    etats.append(dic['state'])
    try:
        ports.append(dic['peer_portprocess'])
    except KeyError:
        pass
    try:
        addr.append(dic['peer_address'])
    except KeyError:
        pass

    f1.write(str(dic))
f1.close()

nbEtats = []
for p in possible : 

    nbEtats.append(etats.count(p))

print(nbEtats)

x = 0
for i in possible :
    
    print(f'état : {i} nombre d entrées dans cet état : {nbEtats[x]}')
    x += 1


print(f'Nombre de "peer_address" : {len(set(addr))} \n Nombre de peer_ports : {len(set(ports))}')

