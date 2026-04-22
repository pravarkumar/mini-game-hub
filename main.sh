#!/bin/bash

clear
touch users.tsv
clear
touch users.tsv

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
RED="\033[1;31m"
RESET="\033[0m"

echo -e "$GREEN"
echo "+------------------------------------------------------+"
echo "|                                                      |"
echo "|   ███╗   ███╗██╗███╗   ██╗██╗                        |"
echo "|   ████╗ ████║██║████╗  ██║██║                        |"
echo "|   ██╔████╔██║██║██╔██╗ ██║██║                        |"
echo "|   ██║╚██╔╝██║██║██║╚██╗██║██║                        |"
echo "|   ██║ ╚═╝ ██║██║██║ ╚████║██║                        |"
echo "|   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝                        |"
echo "|                                                      |"
echo "|    ██████╗  █████╗ ███╗   ███╗███████╗               |"
echo "|   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝               |"
echo "|   ██║  ███╗███████║██╔████╔██║█████╗                 |"
echo "|   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                 |"
echo "|   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗               |"
echo "|    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝               |"
echo "|                                                      |"
echo "|      ██╗  ██╗██╗   ██╗██████╗                        |"
echo "|      ██║  ██║██║   ██║██╔══██╗                       |"
echo "|      ███████║██║   ██║██████╔╝                       |"
echo "|      ██╔══██║██║   ██║██╔══██╗                       |"
echo "|      ██║  ██║╚██████╔╝██████╔╝                       |"
echo "|      ╚═╝  ╚═╝ ╚═════╝ ╚═════╝                        |"
echo "|                                                      |"
echo "|                                                      |"
echo "|                                                      |"
echo "+------------------------------------------------------+"
echo -e "$RESET"
echo

c=0
registered(){
	grep -q "^$1:" users.tsv
}




	while true;
	do
		while true
		do	echo -e "$BLUE=========== 🎮 PLAYER 1 🎮 ===========$RESET"
			printf "${YELLOW}👤 Username: ${RESET}"
			read username

			if [[ "$username" =~ ^[0-9a-zA-Z_]+$ ]]
			then break
			else 
				echo -e "${RED}Invalid username only letters, Numbers, Underscore are allowed!!${RESET}"
			fi
		done

		if registered "$username"
                then
			echo -ne "${YELLOW}🔒 Enter Password: ${RESET}"
			read -s password
			echo
                        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                        stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
                        
			if [ "$hash_pass" == "$stored_pass" ]
                        then
                                echo -e "${GREEN}✅ Login Successful for "$username"!${RESET}"
                                user1="$username"
                                break
                        else
                                echo -e "${RED}❌ Wrong username or password!${RESET}"
                        fi
                else
                               echo -e "${RED}❌ Username does not exist. Do you want to register with this username?(y/n)${RESET}"
			while true
			do
			read s

                        if [[ "$s" == "y" || "$s" == "Y" ]]
                        then
				while true
				do
					echo -ne "${YELLOW}🔒 Create Password: ${RESET}"
					read -s createpass
					echo
					echo -ne "${YELLOW}🔒 Confirm Password: ${RESET}"
					read -s confirmpass
					echo
					if [[ "$createpass" == "$confirmpass" ]]
					then
						break
					else 
						 echo -e "${RED}❌ Passwords don't match. Plz try again.${RESET}"
					fi
				done


				
                                hash_pass1=$(echo -n "$createpass" | sha256sum | cut -d " " -f1)
                                echo "$username":"$hash_pass1">>users.tsv
                                echo -e "${GREEN}✅ Registration Successful for "$username"!${RESET}"
                                user1="$username"
				c=1
                                break
                        elif [[ "$s" == "n" || "$s" == "N" ]]
                        then
				c=2
				break
                        else  echo -e "${RED}❌ Write appropriate characters please.${RESET}"
			
                        fi
		done
		if [[ $c -eq 1 ]]
		then break

		elif [[ $c -eq 2 ]] 
		then continue
		fi	

                fi		
	done

c=0

	while true;
        do
                while true
                do
			echo -e "$BLUE=========== 🎮 PLAYER 2 🎮 ===========$RESET"
			printf "${YELLOW}👤 Username: ${RESET}"

			read username2
			if [[ "$username2" == "$user1" ]]; then
    			echo -e "${RED}❌ Users must be different!${RESET}"
    			continue
			fi

                        if [[ "$username2" =~ ^[0-9a-zA-Z_]+$ ]]
                        then break
                        else
				 echo -e "${RED}❌ "Invalid username only letters, Numbers, Underscore are allowed."${RESET}"
                        fi
                done

                if registered "$username2"
                then
                        echo -ne "${YELLOW}🔒 Enter Password: ${RESET}"
                        read -s password2
                        echo
                        hash_pass2=$(echo -n "$password2" | sha256sum | cut -d " " -f1)
                        stored_pass2=$(grep "^$username2:" users.tsv|cut -d ":" -f2)

                        if [ "$hash_pass2" == "$stored_pass2" ]
                        then
				            echo -e "${GREEN}✅ Login Successful for "$username2"!${RESET}"
                           
                                user2="$username2"
                                break
                        else
                                 echo -e "${RED}❌ Wrong username or password! Please try again.${RESET}"
                        fi
                else
			echo -e "${RED}❌ Username does not exist. Do you want to register with this username?(y/n)${RESET}"
                        while true
                        do
			read s

                        if [[ "$s" == "y" || "$s" == "Y" ]]
                        then
                                while true
                                do
                                          echo -ne "${YELLOW}🔒 Create Password: ${RESET}"
                                        read -s createpass2
                                        echo
                                              echo -ne "${YELLOW}🔒 Confirm Password: ${RESET}"
                                        read -s confirmpass2
                                        echo
                                        if [[ "$createpass2" == "$confirmpass2" ]]
                                        then
                                                break
                                        else
                                                              echo -e "${RED}❌ Passwords don't match. Plz try again.${RESET}"
                                        fi
                                done



                                hash_pass2=$(echo -n "$createpass2" | sha256sum | cut -d " " -f1)
                                echo "$username2":"$hash_pass2">>users.tsv
                                echo -e "${GREEN}✅ Login Successful for "$username2"!${RESET}"
                                user2="$username2"
                                c=1
                                break
                        elif [[ "$s" == "n" || "$s" == "N" ]]
                        then
                                c=2
                                break
                             else  echo -e "${RED}❌ Write appropriate characters please.${RESET}"

                        fi
                done
                if [[ $c -eq 1 ]]
                then break

                elif [[ $c -eq 2 ]]
                then continue
                fi

                fi
        done

	echo -e "$BLUE=========== ⚔️🛡️✨ STARTING GAME ⚔️🛡️✨ ===========$RESET"

echo
echo -e "${GREEN}💻 Player 1: $username${RESET}"
echo -e "${GREEN}💻 Player 2: $username2${RESET}"

echo
echo -ne "${YELLOW}⏳ Loading: ["
for i in {1..20}; do
    echo -ne "█"
    sleep 0.15
done
echo -e "]${RESET}"

echo
python game.py "$username" "$username2"
