#!/bin/bash


touch users.tsv

c=0
registered(){
	grep -q "^$1:" users.tsv
}




	while true;
	do
		while true
		do
			echo -n "Enter Username of Player 1: "
			read username

			if [[ "$username" =~ ^[0-9a-zA-Z_]+$ ]]
			then break
			else 
				echo "Invalid username only letters, Numbers, Underscore are allowed."
			fi
		done

		if registered "$username"
                then
			echo -n "Enter Password: "
			read -s password
			echo
                        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                        stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
                        
			if [ "$hash_pass" == "$stored_pass" ]
                        then
                                echo Login Successful for "$username"!
                                user1="$username"
                                break
                        else
                                echo Wrong username or password! Please try again.
                        fi
                else
                        echo "Username does not exist. Do you want to register with this username?(y/n)"
			while true
			do
			read s

                        if [[ "$s" == "y" || "$s" == "Y" ]]
                        then
				while true
				do
					echo -n "Create Password: "
					read -s createpass
					echo
					echo -n "Confirm Password: "
					read -s confirmpass
					echo
					if [[ "$createpass" == "$confirmpass" ]]
					then
						break
					else 
						echo "Passwords do not match. Please try again."
					fi
				done


				
                                hash_pass1=$(echo -n "$createpass" | sha256sum | cut -d " " -f1)
                                echo "$username":"$hash_pass1">>users.tsv
                                echo "Registration Successful for "$username"!"
                                user1="$username"
				c=1
                                break
                        elif [[ "$s" == "n" || "$s" == "N" ]]
                        then
				c=2
				break
                        else echo "Write appropriate character."
			
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
			echo -n "Enter Username of Player 2: "
			read username2
			if [[ "$username2" == "$user1" ]]; then
    			echo "Player 2 must be different from Player 1"
    			continue
			fi

                        if [[ "$username2" =~ ^[0-9a-zA-Z_]+$ ]]
                        then break
                        else
                                echo "Invalid username only letters, Numbers, Underscore are allowed."
                        fi
                done

                if registered "$username2"
                then
                        echo -n "Enter Password: "
                        read -s password2
                        echo
                        hash_pass2=$(echo -n "$password2" | sha256sum | cut -d " " -f1)
                        stored_pass2=$(grep "^$username2:" users.tsv|cut -d ":" -f2)

                        if [ "$hash_pass2" == "$stored_pass2" ]
                        then
                                echo "Login Successful for "$username2"!"
                                user2="$username2"
                                break
                        else
                                echo Wrong username or password! Please try again.
                        fi
                else
                        echo "Username does not exist. Do you want to register with this username?(y/n)"
                        while true
                        do
			read s

                        if [[ "$s" == "y" || "$s" == "Y" ]]
                        then
                                while true
                                do
                                        echo -n "Create Password: "
                                        read -s createpass2
                                        echo
                                        echo -n "Confirm Password: "
                                        read -s confirmpass2
                                        echo
                                        if [[ "$createpass2" == "$confirmpass2" ]]
                                        then
                                                break
                                        else
                                                echo "Passwords do not match. Please try again."
                                        fi
                                done



                                hash_pass2=$(echo -n "$createpass2" | sha256sum | cut -d " " -f1)
                                echo "$username2":"$hash_pass2">>users.tsv
                                echo "Registration Successful for "$username2"!"
                                user2="$username2"
                                c=1
                                break
                        elif [[ "$s" == "n" || "$s" == "N" ]]
                        then
                                c=2
                                break
                        else echo "Write appropriate character."

                        fi
                done
                if [[ $c -eq 1 ]]
                then break

                elif [[ $c -eq 2 ]]
                then continue
                fi

                fi
        done

	echo "Starting game for "$user1" and "$user2""

	#python3 game.py
