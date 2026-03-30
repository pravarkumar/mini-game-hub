#!/bin/bash

clear
touch users.tsv

GREEN="\033[1;32m"
YELLOW="\033[1;33m"
BLUE="\033[1;34m"
RED="\033[1;31m"
RESET="\033[0m"

echo -e "$GREEN"
echo "========================================================"
echo "                                                        "
echo "               🎮 MINI GAME HUB 🎮                    "
echo "                                                        "
echo "        🕹️  Play • Compete • Have Fun  🕹️             "
echo "                                                        "
echo "========================================================"
echo -e "$RESET"

echo

registered(){
    grep -q "^$1:" users.tsv
}

while true;
do
    echo -e "$BLUE=========== 🎮 PLAYER 1 🎮 ===========$RESET"
    printf "${YELLOW}👤 Username: ${RESET}"
    read username

    echo -ne "${YELLOW}🔒 Password: ${RESET}"
    read -s password
    echo

    if registered "$username"
    then
        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
        stored_pass=$(grep "^$username:" users.tsv | cut -d ":" -f2)

        if [ "$hash_pass" == "$stored_pass" ]
        then
            echo -e "${GREEN}✅ Login Successful!${RESET}"
            user1="$username"
            break
        else
            echo -e "${RED}❌ Wrong username or password!${RESET}"
        fi
    else
        echo -e "${RED}❌ Username does not exist. Register? (y/n)${RESET}"
        read s

        if [ "$s" == "y" ]
        then
            hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
            echo "$username":"$hash_pass1" >> users.tsv

            echo -e "${GREEN}✅ Registration Successful!${RESET}"
            user1="$username"
            break

        elif [ "$s" == "n" ]
        then
            continue
        else
            echo -e "${RED}❌ Invalid input!${RESET}"
        fi
    fi
done

echo

while true;
do
    echo -e "$BLUE=========== 🎮 PLAYER 2 🎮 ===========$RESET"
    printf "${YELLOW}👤 Username: ${RESET}"
    read username

    echo -ne "${YELLOW}🔒 Password: ${RESET}"
    read -s password
    echo

    if [ "$username" == "$user1" ]
    then
        echo -e "${RED}❌ Users must be different!${RESET}"
        continue
    fi

    if registered "$username"
    then
        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
        stored_pass=$(grep "^$username:" users.tsv | cut -d ":" -f2)

        if [ "$hash_pass" == "$stored_pass" ]
        then
            echo -e "${GREEN}✅ Login Successful!${RESET}"
            user2="$username"
            break
        else
            echo -e "${RED}❌ Wrong username or password!${RESET}"
        fi
    else
        echo -e "${RED}❌ Username does not exist. Register? (y/n)${RESET}"
        read s

        if [ "$s" == "y" ]
        then
            hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
            echo "$username":"$hash_pass1" >> users.tsv

            echo -e "${GREEN}✅ Registration Successful!${RESET}"
            user2="$username"
            break

        elif [ "$s" == "n" ]
        then
            continue
        else
            echo -e "${RED}❌ Invalid input!${RESET}"
        fi
    fi
done

echo

echo -e "$GREEN=========== 🚀 STARTING GAME 🚀 ===========$RESET"

echo
echo -e "${GREEN}🎯 Player 1: $user1${RESET}"
echo -e "${GREEN}🎯 Player 2: $user2${RESET}"

echo
echo -ne "${YELLOW}⏳ Loading: ["
for i in {1..20}; do
    echo -ne "█"
    sleep 0.05
done
echo -e "]${RESET}"

echo
python3 game.py "$user1" "$user2"
