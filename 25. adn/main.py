# A.1 = découper fichier texte en séquence de 3 éléments
# - dans un tableau 
# - chaque entrée = 1 séquence 

# Importer fichier texte 

def import_txt (file) :
    f = open(file, 'r')
    content = f.read()
    # print(content)
    return content

adn = import_txt('adn.txt')

# Découpe 

def split_adn(protein, sequence):
  return [protein[i:i+sequence] for i in range(0, len(protein), sequence)]

print(split_adn(adn, 3))