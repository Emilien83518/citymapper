import json

# Load your file
with open('paris.json', 'r') as file:
    f = json.load(file)

def isstop(g, fi):
    """Returns a list of all lines passing through station g."""
    found_lines = []
    for line_id in fi['lignes']:
        if g in fi['lignes'][line_id]["stations"]:
            found_lines.append(line_id)
    return found_lines if found_lines else "stop does not exist"
print(isstop("Triolo",f))
def isconnect(acs, fi):
    """Returns lines available for transfer at station acs."""
    for item in fi.get("correspondances", []):
        if acs == item["station"]:
            return item["lignes"]
    return []

def dicostop(L):
    """Creates a dictionary mapping each station to its neighbors and transfers."""
    if L not in f['lignes']:
        return "Line not found"
        
    st = f['lignes'][L]['stations']
    ligne_map = {}
    
    for u in range(len(st)):
        current_station = st[u]
        neighbors = []
        
        # Add previous station
        if u > 0:
            neighbors.append(st[u-1])
        else:
            neighbors.append('no stop')
        
        # Add next station
        if u < len(st) - 1:
            neighbors.append(st[u+1])
        else:
            neighbors.append('no stop')
            
        # Add transfer lines
        transfers = isconnect(current_station, f)
        if transfers:
            neighbors.append(transfers)
            
        ligne_map[current_station] = neighbors
        
    return ligne_map

def path(start, nl, l):
    pa = [start]  # Start by adding the current station to the path
    
    # Check if the target line (nl) is available at the current station's transfers
    if nl in l[start][-1]: 
        return pa
        
    # If there is no next station (it's the end of the line), stop searching
    # (Checking len(l[start]) < 2 handles terminal stations safely)
    if len(l[start]) < 2 or isinstance(l[start][1], list):
        return False
    else:
        # Recursively find the path from the next station
        next_path = path(l[start][1], nl, l)
        
        if next_path:  # If a path was found downstream, combine it
            return pa + next_path
        return False
    
def pathend(start,end,l):
    pa=[start]
    if l[start][1]==end:
        return pa
    if len(l[start]) < 2 or isinstance(l[start][1], list):
        return False
    else:
        # Recursively find the path from the next station
        next_path = pathend(l[start][1], end, l)
        
        if next_path:  # If a path was found downstream, combine it
            return pa + next_path
        return False
# Execution
start = input('Start station: ')
end = input('End station: ')
print(start)
lignestart = isstop(start, f)
ligneend = isstop(end, f)

print(f"Lines for {start}: {lignestart}")
print(f"Lines for {end}: {ligneend}")

dicostart=dicostop(lignestart[0])
dicoend=dicostop(ligneend[0])
arret=path(start,ligneend[0],dicostart)
print(arret)
lol=pathend(arret[-1],end,dicoend)
print(lol)
