#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if((len(string) % 2) == 0):
        return True

    return False

def remove_third_char(string: str) -> str:
    resultat = ""
    for k in range(0, len(string)):
        if k == 2:
            continue
        resultat += string[k]
    return resultat


def replace_char(string: str, old_char: str, new_char: str) -> str:
    resultat = ""

    for k in range(0, len(string)):
        if string[k] == old_char:
            resultat += new_char
            continue

        resultat += string[k]

    return resultat


def get_number_of_char(string: str, char: str) -> int:
    resultat = 0

    for lettre in string:
        if lettre == char:
            resultat += 1

    return resultat


def get_number_of_words(sentence: str, word: str) -> int:
    resultat = 0

    for k in range(0,len(sentence)):
        if sentence[k] == word[0]:
            #Verifier si le mot est trop long pour rentrer entre la fin de la chaine et la ou on est
            if len(sentence) < k + len(word):
                break

            #Verifier le mot
            for j in range(1,len(word)):
                if sentence[k+j] != word[j]:
                    k += j
                    break
                if j == len(word)-1:
                    k += j
                    resultat += 1
    return resultat

def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo do"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
