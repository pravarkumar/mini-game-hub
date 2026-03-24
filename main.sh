#!/bin/bash


touch users.tsv


registered(){
	grep -q "^$1:" users.tsv
}




	while true;
	do
		echo -n "Enter Username of Player 1:"
		read username
		echo -n "Enter Password:"
		read -s password
		echo
		if registered "$username"
		then
			hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
			stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
			if [ "$hash_pass" == "$stored_pass" ]
			then
				echo Login Successful!
				user1="$username"
				break
			else
				echo Wrong username or password! Please try again.
			fi
		else
			echo "Username does not exist. Do you want to register?(y/n)"
			read s
			if [ "$s" == "y" ]
			then
				hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
				echo "$username":"$hash_pass1">>users.tsv
			        echo "Registration Successful!"
				user1="$username"
				break
			elif [ "$s" == "n" ]
			then continue


			else echo "Write appropriate character."
			fi
		fi
	done



	while true;
        do
                echo -n "Enter Username of Player 2:"
                read username
                echo -n "Enter Password:"
                read -s password
                echo


		if [ "$username" == "$user1" ]
		then
			echo "Users must be different, Please try again."
			continue
		fi

                if registered "$username"
                then
                        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                        stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
                        if [ "$hash_pass" == "$stored_pass" ]
                        then
                                echo Login Successful!
                                user2="$username"
                                break
                        else
                                echo Wrong username or password! Please try again.
                        fi
                else
                        echo "Username does not exist. Do you want to register?(y/n)"
                        read s
                        if [ "$s" == "y" ]
                        then
                                hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                                echo "$username":"$hash_pass1">>users.tsv
                                echo "Registration Successful!"
                                user2="$username"
                                break
                        elif [ "$s" == "n" ]
                        then continue


                        else echo "Please write appropriate character."
                        fi
                fi
        done
	

	


	echo "Starting the game for $user1 and $user2."
	# python3 game.py "$user1" "$user2"

	

			


