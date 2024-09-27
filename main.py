"""
fonctions itérative et récursive de artcode
"""

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    li=[]
    o=1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            o+=1
        else:
            x=(s[i-1],o)
            li.append(x)
            o=1
    li.append((s[-1],o))
    return li

l=[]
def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
       en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s)==0:
        return l
    i=0
    c=s[0]
    while i<len(s) and c==s[i]:
        i+=1
    l.append((c,i))
    return artcode_r(s[i:])
#### Fonction principale


def main():
    """
    test des fonctions
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('~~~~~@@@---@@@~~~~~'))

if __name__ == "__main__":
    main()
