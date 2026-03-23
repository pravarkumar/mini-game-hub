#!/bin/bash
echo "Player 1:"
read u1 #Info of Player 1 

echo "Player 2:"
read u2 #Info of PLayer 2 
python3 game.py

authenticated=0

while [ $authenticated -eq 0 ]
do
    echo "Enter username:"
    read username

    echo "Enter password:"
    read password

    python3 auth.py "$username" "$password"

    if [ $? -eq 0 ]; then
        authenticated=1
    else
        echo "Try again"
    fi
done

