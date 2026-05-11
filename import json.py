import json
with open('lille.json','r') as file:
    f = json.load(file)
#fais un dico de la ligne choisi arret par arret
def dicostop(L):
    st=[]
    for station in f['lignes'][L]['stations']:
        st.append(station)
    ligne1={st[0]:[st[1]]}
    a=1
    for u in range(1,len(st)):
        if st[u]==st[-1]:
            ligne1[st[u]]=[st[u-1]]
        else:
            ligne1[st[u]]=[st[u-1],st[u+1]]
    return ligne1

k=dicostop("R")
print(k)

def isstop(g,fi):
    for i in fi['lignes']:
            for y in fi['lignes'][i]["stations"]:
                return i
    return 'stop does not exist'


def path(de,lde,l,f):
    path=[]
    if isconnect(de,l,f)==de:
        return path
    else:
        path.append(lde[de][1])
        return path(lde[de][1])

# verifie les correspondance
def isconnect(acs,wl,f):
    for i in range(0,len(f["correspondances"])):
        if acs==f["correspondances"][i]["station"]:
            for a in range(0,len(f["correspondances"][i]["lignes"])):
                if wl ==  f["correspondances"][i]["lignes"][a]:
                    return f["correspondances"][i]["station"]
                else:
                    return "the correspondance do not exist"
    return "this stop don't have any correspondance"

Depart=input("start location")
arrivée=input("arriving location")

lignedepart=isstop(Depart,f)
lignearrivée=isstop(arrivée,f)
listelignedepart= dicostop(lignedepart)
listelignearrivée=dicostop(lignearrivée)
p=path(Depart,listelignedepart,lignearrivée,f)
print(p)




def dfs(G, s):
    colour = dict()
    for x in G:
        colour[x] = 'white'
    path = [s]
    colour[s] = 'grey'
    stack = [s]
    while stack != []:
        current = stack[-1]
        white_neighbours = [v for v in G[current]
                            if colour[v] == 'white']
    if white_neighbours != []:
        v = white_neighbours[0]
        colour[v] = 'grey'
        path.append(v)
        stack.append(v)
    else:
        stack.pop()
        colour[current] = 'black'
    return path