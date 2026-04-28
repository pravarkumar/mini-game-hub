#!/bin/bash
#colors to be used in the game hub
BOLD="\033[1m"
DIM="\033[2m"
BLINK="\033[5m"
RESET="\033[0m"

# Even more impressive colors to be used in the game hub
NEON_CYAN="\033[1;96m"
NEON_PINK="\033[1;95m"
NEON_GREEN="\033[1;92m"
NEON_YELLOW="\033[1;93m"
NEON_BLUE="\033[1;94m"
NEON_RED="\033[1;91m"
WHITE="\033[1;97m"
GRAY="\033[0;90m"
DARK_CYAN="\033[0;36m"

# Background thingies (if we want them)
BG_BLUE="\033[44m"
BG_MAGENTA="\033[45m"


sleep_fast() { sleep "${1:-0.05}"; }
# I wanted to create a sleep fucntion like the inbuilt sleep function which also has a defualt value like if no argument is given the program sleep for like 0.5 


#Needed to centerise the etx to look aesthatic 
center_text() {
    local text="$1"
    # Local means the scope of the variale is within the fucntion only it dies the moment we go outside the function
    #Assumed a terminal width of 80 characters for centering. You can adjust this as needed or make it dynamic.
    local width=80
    local text_clean
    text_clean=$(echo -e "$text" | sed 's/\x1B\[[0-9;]*m//g')
    #Whatever the tex is we want to calculate the actual thing and not the color part so we are removing the color part and then calculating the length of the text and then we are calculating the padding by subtracting the length of the text from the width and dividing it by 2 and then we are printing that many spaces before the text to center it
    local len=${#text_clean}
    local pad=$(( (width - len) / 2 ))
    printf "%${pad}s" ""
    #Centering the text by printing the padding spaces before the text and then printing the text
    echo -e "$text"
}

 #RESET is like bring back the formatting to normal color mode

divider() {
    local color="${1:-$GRAY}"
    local width=80
    echo -e "${color}$(printf '━%.0s' $(seq 1 $width))${RESET}"
}

# The following is a function which makes the text come character by charcter making it cooler :)
typewrite() {
    #Need to read char by char  
    local color="$1"
    local text="$2"
    local delay="${3:-0.03}"
    echo -ne "$color"
    #${#text} is the length of the text 
    for ((i=0; i<${#text}; i++)); do 
        echo -ne "${text:$i:1}"
        #{variable :start :end}  
        sleep "$delay"
        #delay for the next char 
    done
    echo -e "$RESET"
}

# We boot here 
boot_sequence() {
    clear
    echo 
    echo -e "${NEON_RED}${BOLD}Booting up the Game Hub...${RESET}"
    sleep 1.5
    echo
    center_text "${NEON_YELLOW}${BOLD}███╗   ███╗██╗███╗   ██╗██╗${RESET}"
    center_text "${NEON_YELLOW}${BOLD}████╗ ████║██║████╗  ██║██║${RESET}"
    center_text "${NEON_YELLOW}${BOLD}██╔████╔██║██║██╔██╗ ██║██║${RESET}"
    center_text "${NEON_YELLOW}${BOLD}██║╚██╔╝██║██║██║╚██╗██║██║${RESET}"
    center_text "${NEON_YELLOW}${BOLD}██║ ╚═╝ ██║██║██║ ╚████║██║${RESET}"
    center_text "${NEON_YELLOW}${BOLD}╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝${RESET}"
    echo
    center_text "${NEON_PINK}${BOLD} ██████╗  █████╗ ███╗   ███╗███████╗${RESET}"
    center_text "${NEON_PINK}${BOLD}██╔════╝ ██╔══██╗████╗ ████║██╔════╝${RESET}"
    center_text "${NEON_PINK}${BOLD}██║  ███╗███████║██╔████╔██║█████╗  ${RESET}"
    center_text "${NEON_PINK}${BOLD}██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ${RESET}"
    center_text "${NEON_PINK}${BOLD}╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗${RESET}"
    center_text "${NEON_PINK}${BOLD} ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝${RESET}"
    echo
    center_text "${NEON_CYAN}${BOLD}       ██╗  ██╗██╗   ██╗██████╗     ${RESET}"
    center_text "${NEON_CYAN}${BOLD}       ██║  ██║██║   ██║██╔══██╗    ${RESET}"
    center_text "${NEON_CYAN}${BOLD}       ███████║██║   ██║██████╔╝    ${RESET}"
    center_text "${NEON_CYAN}${BOLD}       ██╔══██║██║   ██║██╔══██╗    ${RESET}"
    center_text "${NEON_CYAN}${BOLD}       ██║  ██║╚██████╔╝██████╔╝    ${RESET}"
    center_text "${NEON_CYAN}${BOLD}       ╚═╝  ╚═╝ ╚═════╝ ╚═════╝    ${RESET}"
    echo

    echo

    divider "$NEON_YELLOW"
    center_text "${NEON_WHITE}[ VERSION 3.0 ]  ·  [ TWO PLAYER ]  ·  [ SHA-256 SECURED ]  ${RESET}"
    divider "$NEON_YELLOW"

    echo
    center_text "${NEON_GREEN}${BLINK}▶  SYSTEM INITIALIZING  ◀${RESET}"
    echo

    # Formalities of booting up with some cool logs and stuff
    local logs=(
        "Loading game engine................"
        "Mounting user database.............."
        "Injecting color engine.............."
        "Arming player collision module......"
        "Calibrating fun levels.............."
        "Engaging hype mode.................."
    )
    #cuz why not 
    for log in "${logs[@]}"; do
        echo -ne "  ${GRAY}${log}${RESET}"
        sleep 0.2
        echo -e " ${NEON_GREEN}[ OK ]${RESET}"
    done
    
    echo
    sleep 0.3
    typewrite "$NEON_CYAN" "  ► All systems operational. Welcome, challengers." 0.025
}

section_header() {
    local title="$1"
    local color="${2:-$NEON_CYAN}"
    echo
    divider "$WHITE"
    center_text "${color}${BOLD}  ◈  ${title}  ◈  ${RESET}"
    divider "$WHITE"
    echo
}


fancy_prompt() {
    local icon="$1"
    local label="$2"
    local varname="$3"
    echo -ne "  ${NEON_YELLOW}${icon} ${label}: ${RESET}${WHITE}"
    read -r "$varname"
    echo -ne "$RESET"
}

secret_prompt() {
    local icon="$1"
    local label="$2"
    local varname="$3"
    echo -ne "  ${NEON_YELLOW}${icon} ${label}: ${RESET}"
    read -rs "$varname"
    echo
}

# Status Messages
ok()    { echo -e "  ${NEON_GREEN}${BOLD}✔  $*${RESET}"; }
fail()  { echo -e "  ${NEON_RED}${BOLD}✘  $*${RESET}"; }
info()  { echo -e "  ${NEON_BLUE}❕  $*${RESET}"; }
warn()  { echo -e "  ${NEON_YELLOW}⚠️ $*${RESET}"; }

# Auth check
registered() {
    grep -q "^$1:" users.tsv 
    #0 success  / 1 faliure 
}

# Auth Flow for one player
auth_player() {
    local player_num="$1"
    local other_user="$2"      # already logged-in user to prevent duplicate
    local result_var="$3"
    local icons=("💻")
    local icon="${icons[0]}"
    local c=0

    while true; do
        section_header "${icon}  PLAYER ${player_num} — IDENTIFY YOURSELF" "$NEON_YELLOW"

        # ── Username ──
        while true; do
            fancy_prompt "👤" "Username" username_input
            if [[ -z "$username_input" ]]; then
                fail "Username cannot be empty."
                # -z is used to check if the string is empty or not
                continue
            fi

            if [[ "$username_input" == "$other_user" ]]; then
                fail "That player is already in the match! Choose a different account."
                continue
            fi

            if [[ "$username_input" =~ ^[0-9a-zA-Z_]+$ ]]; then
                break
            else
                fail "Invalid username — only letters, numbers, and underscores allowed."
            fi

        done

        # ── Login or Register ──
        if registered "$username_input"; then
            divider "$WHITE"
            info "Account found. Enter your password."
            secret_prompt "🔒" "Password" pass_input
            hash_input=$(echo -n "$pass_input" | sha256sum | cut -d ' ' -f1)
            stored=$(grep "^${username_input}:" users.tsv | cut -d ':' -f2)

            if [[ "$hash_input" == "$stored" ]]; then
                ok "Login successful — Welcome back, ${BOLD}${username_input}${RESET}${NEON_GREEN}!"
                sleep 0.3
                printf -v "$result_var" "%s" "$username_input"
                return
            else
                fail "Wrong password. Try again."
                continue
            fi

        else
            divider "$WHITE"
            warn "No account found for '${username_input}'."
            echo
            echo -ne "  ${NEON_PINK}▸ Register a new account? ${GRAY}[y/n]${RESET}: "
            read -r choice

            if [[ "$choice" =~ ^[Yy]$ ]]; then
                # Password creation loop
                while true; do
                    secret_prompt "🔑" "Create Password" new_pass
                    secret_prompt "🔑" "Confirm Password" confirm_pass
                    if [[ "$new_pass" == "$confirm_pass" ]]; then
                        break
                    else
                        fail "Passwords don't match. Try again."
                    fi
                done

                new_hash=$(echo -n "$new_pass" | sha256sum | cut -d ' ' -f1)
                echo "${username_input}:${new_hash}" >> users.tsv
                ok "Account created! Welcome, ${BOLD}${username_input}${RESET}${NEON_GREEN}!"
                sleep 0.3
                printf -v "$result_var" "%s" "$username_input"
                return

            elif [[ "$choice" =~ ^[Nn]$ ]]; then
                info "Returning to username entry..."
                sleep 0.3
                continue
            else
                warn "Please answer y or n."
                sleep 0.2
                continue
            fi
        fi
    done
}

match_intro() {
    local p1="$1"
    local p2="$2"
    clear
    echo
    center_text "${NEON_YELLOW}${BOLD}  ⚔  THE MATCH IS SET  ⚔  ${RESET}"
    echo

    center_text "${WHITE}${BOLD}${p1}${RESET} ${RED}${BOLD}VS${RESET}${WHITE}${BOLD} ${p2}${RESET}"
    echo
    divider "$WHITE"
    echo

    # basic pattern here 
    echo -ne "  ${NEON_YELLOW}⏳ Charging up${RESET}  ${NEON_CYAN}["
    BAR_WIDTH=40
    for ((i=1; i<=BAR_WIDTH; i++)); do
        if (( i < BAR_WIDTH * 4 / 10 )); then
            echo -ne "${NEON_GREEN}█"
        elif (( i < BAR_WIDTH * 7 / 10 )); then
            echo -ne "${NEON_YELLOW}█"
        else
            echo -ne "${NEON_RED}█"
        fi
        sleep 0.045
    done
    echo -e "${NEON_CYAN}]  ${NEON_GREEN}READY!${RESET}"
    echo

    # Countdown begins for the game to start
    for n in 3 2 1; do
        echo -ne "\r  "
        #\r -> go back to very start fo this line  
        case $n in
            3) echo -ne "${NEON_YELLOW}${BOLD}  ● ● ●  GET READY...  ${RESET}" ;;
            2) echo -ne "${NEON_PINK}${BOLD}  ● ●    STEADY...     ${RESET}" ;;
            1) echo -ne "${NEON_RED}${BOLD}  ●       GO!          ${RESET}" ;;
        esac
        sleep 0.7
        echo
    done

    echo
    center_text "${WHITE}${BOLD}▓▓▓  L A U N C H I N G   G A M E  ▓▓▓${RESET}"
    echo
    sleep 0.5
}
# finally at the main part huh ..

boot_sequence 
# main part of booting is called here  

# Player 1 auth
auth_player 1 "" user1

# Player 2 auth  
auth_player 2 "$user1" user2

match_intro "$user1" "$user2"

python3 game.py "$user1" "$user2"
