#coding:utf-8

print("\nTon mot de passe doit contenir au minimum 8 caractères.")
print("Ton mot de passe doit contenir au minimum 1 lettre en minuscule.")
print("Ton mot de passe doit contenir au minimum 1 lettre en majuscule.")
print("Ton mot de passe doit contenir au minimum 1 chiffre.")
print("Ton mot de passe ne doit pas contenir d'espace.")
print("Ton mot de passe ne doit pas contenir de caractères spéciaux.\n")
print("À présent, entre ton mot de passe.\n")

password = input("Mot de passe : ")

lowerAlphabet = "abcdefghijklmnopqrstuvwxyz"
upperAlphabet = lowerAlphabet.upper()
numbers = "1234567890"

lowerCounter = 0                         
upperCounter = 0                        
numberCounter = 0                       
spacebarFlag = False                    
specialCharactersFlag = False          
specialCharacters = []                  
conditionsSatisfied = True             
 

length = len(password)
for ch in password:
    if ch in lowerAlphabet:                    
       lowerCounter += 1
    elif ch in upperAlphabet:
        upperCounter +=1
    elif ch in numbers:
        numberCounter += 1
    elif ch == ' ':
        spacebarFlag = True
    else:
        specialCharactersFlag = True
        specialCharacters.append(ch)                       


if len(password) < 8:
    conditionsSatisfied = False
if lowerCounter == 0:
    conditionsSatisfied = False
if upperCounter == 0:
    conditionsSatisfied = False
if numberCounter == 0:
    conditionsSatisfied = False
if spacebarFlag:
    conditionsSatisfied = False                    
if specialCharactersFlag:
    conditionsSatisfied = False


if not conditionsSatisfied:
    print("\nMot de passe incorrect : " + password + "\n")
    if len(password) < 8:
        print("\tTon mot de passe contient que", "" + str(len(password)) + "", "caractère(s).")
    if lowerCounter == 0:
        print("\tTu as oublié(e) de mettre une minuscule.")
    if upperCounter == 0:
        print("\tTu as oublié(e) de mettre une majuscule.")
    if numberCounter == 0:
        print("\tTu as oublié(e) de mettre un chiffre.")
    if spacebarFlag:
        print("\tTu ne dois pas mettre d'espace.")
    if specialCharactersFlag:
        print("\tTon mot de passe a des caractères spéciaux : " + ''.join(map(str, specialCharacters)) + "\n")


else:
    print("Mot de passe correct. Confirme ce mot de passe. Tu as 3 essais.")
    confirmationTries = 0
    while confirmationTries < 3:                                        
        passwordConfirmation = input("Confirmer votre mot de passe : ")       
        if password != passwordConfirmation:                        
            confirmationTries += 1
        else:                                                    
            print("\nTu as enfin un mot de passe solide !\nTon mot de passe est : " + password)
            break
            
            
    if confirmationTries == 3:                                 
        print()
        print("La création du mot de passe a échouée.\n")
        print("Mot de passe : " + password)
        print("Le mot de passe ne correspond pas.")
