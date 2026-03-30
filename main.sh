#!/bin/bash


touch users.tsv


registered(){
	grep -q "^$1:" users.tsv
}




	while true;
	do
		printf "\033[1;33mEnter Username of Player 1:\033[0m"
		read username
		echo -ne "\033[1;35mEnter Password\033[0m"
		read -s password
		echo
		if registered "$username"
		then
			hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
			stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
			if [ "$hash_pass" == "$stored_pass" ]
			then
				 echo -e "\033[1;32mLogin Successful!\033[0m"
				user1="$username"
				break
			else
				echo -e "\033[1;31mWrong username or password! Please try again.\033[0m"
			fi
		else
			echo -e "\033[1;31mUsername does not exist. Do you want to register?(y/n)\033[0m"
			read s
			if [ "$s" == "y" ]
			then
				hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
				echo "$username":"$hash_pass1">>users.tsv
			         echo -e "\033[1;32mRegistration Successful!!\033[0m"
				user1="$username"
				break
			elif [ "$s" == "n" ]
			then continue


			 echo -e "\033[1;32mRegistration Successful!!\033[0m"
			fi
		fi
	done



	while true;
        do
               printf "\033[1;33mEnter Username of Player 2:\033[0m"
                read username
                  echo -ne "\033[1;35mEnter Password\033[0m"
                read -s password
                echo


		if [ "$username" == "$user1" ]
		then
			 echo -e "\033[1;31mUsers must be different, Please try again.\033[0m"
			continue
		fi

                if registered "$username"
                then
                        hash_pass=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                        stored_pass=$(grep "^$username:" users.tsv|cut -d ":" -f2)
                        if [ "$hash_pass" == "$stored_pass" ]
                        then
                                echo -e "\033[1;32mLogin Successful!\033[0m"
                                user2="$username"
                                break
                        else
				 echo -e "\033[1;31mWrong username or password! Please try again.\033[0m"
                        fi
                else
                        echo -e "\033[1;31mUsername does not exist. Do you want to register?(y/n)\033[0m"
                        read s
                        if [ "$s" == "y" ]
                        then
                                hash_pass1=$(echo -n "$password" | sha256sum | cut -d " " -f1)
                                echo "$username":"$hash_pass1">>users.tsv
                                echo -e "\033[1;32mRegistration Successful!!\033[0m"
                                user2="$username"
                                break
                        elif [ "$s" == "n" ]
                        then continue


                        else echo -e "\033[1;31mPlease write appropriate character.\033[0m"
                        fi
                fi
        done
	

	

	echo -e "\033[1;36mStarting the game for $user1 and $user2.\033[0m"
	echo 
	# python3 game.py "$user1" "$user2"
	echo -e "\033[1;32mWelcome to Mini Game Hub!\033[0m"
		

			


