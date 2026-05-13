import json
with open('lille.json','r') as file:
    f = json.load(file)
#fais un dico de la ligne choisi arret par arret
def dicostop(L):
    st=[]
    l=[]
    for station in f['lignes'][L]['stations']:
        st.append(station)
    ligne1={st[0]:[st[1],isconnect(st[0],f)]}
    for u in range(1,len(st)):
        if st[u]==st[-1]:
            l=[st[u-1]]
            l.append(isconnect(st[u],f))
            ligne1[st[u]]=l
        else:
            l=[st[u-1],st[u+1]]
            l.append(isconnect(st[u],f))
            ligne1[st[u]]=l
    return ligne1


def isstop(g,fi):
    for i in fi['lignes']:
            for y in fi['lignes'][i]["stations"]:
                    if y == g:
                        return i
    return 'stop does not exist'

# verifie les correspondance
def isconnect(acs, f):
    for item in f.get("correspondances", []):
        if acs == item["station"]:
            return item["lignes"]
    return []
    
k=dicostop("R")
b=isconnect('Gare Lille Flandres',f)
print(b)
print(k)