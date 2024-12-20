# A.1 = découper fichier texte en séquence de 3 éléments
# - dans un tableau 
# - chaque entrée = 1 séquence 

# Importer fichier texte 

import json

def import_txt (file) :
    f = open(file, 'r')
    content = f.read()
    # print(content)
    return content

adn = import_txt('adn.txt')

# Découpe 

def get_codon(elem, sequence):
  return [elem[i:i+sequence] for i in range(0, len(elem), sequence)]

#print(get_codon(adn, 3))

sequenced_table = get_codon(adn, 3)

# A.2 traduire les codons en proteines

#Recupérer json 
with open("table_codon.json", "r") as f:
    table_codon = json.load(f)

#print(table_codon)

# Associer protein => codon

def get_protein(codons, proteins): 
    conversion = []
    for codon in codons:
        converted = proteins.get(codon)
        conversion.append(converted)
    return ' '.join(str(e) for e in conversion) 

# print(get_protein(sequenced_table,table_codon ))


#B.1 Découpe en séquences de 25 éléments
def get_consensus(elems, n):
    consensus_table = get_codon(elems, n)
    return ' '.join(str(e) for e in consensus_table)

# print(get_consensus(adn))
consensus = get_consensus(adn, 25)
# print(consensus)

# B.2 redécouper ces "groupes" en 5 séquences de 5 nucléotides

def get_nucleotides(elems):
    result_nuc = ''
    nuc = get_consensus(elems, 5)
    separated_nuc = nuc.split(' ') 
    for i in separated_nuc : 
            result_nuc= " ".join(i) 
            print(result_nuc)
    return result_nuc

nucleotide_sequence = get_nucleotides(adn)
# print(nucleotide_sequence)

#B.3 Calcul récurrence de chaque séquence façon suite de Conway 




