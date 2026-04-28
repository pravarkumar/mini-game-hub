#!/bin/bash
# leaderboard.sh - reads history.csv and shows formatted leaderboard
# Usage: bash leaderboard.sh [wins|losses|ratio]

PARAMETER="$1"
HISTORY="history.csv"


GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RESET="\033[0m"

echo -e "${GREEN}========== 🏆 LEADERBOARD 🏆 ==========${RESET}"
echo -e "${YELLOW}Sorted by: $PARAMETER${RESET}"
echo
awk -F',' -v sort_by="$PARAMETER" '
NR {
    p1=$1
    p2=$2
    game =$3
    result =$4

    if (result == "draw") {
        draws[game][p1]++
        draws[game][p2]++
        next
    }

    wins[game][p1]++
    losses[game][p2]++
}
END {
    
    for (g in wins){
        i=0
        delete data
        delete seen
        delete key
        delete idx
        print "Game: " g
        printf "%-20s %-8s %-8s %-8s %-8s\n", "Player", "Wins", "Losses", "Draws", "W/L Ratio"
        print "----------------------------------------------------------------"

        for (p in wins[g]) seen[p] = 1
        for (p in losses[g]) seen[p] = 1
        for (p in draws[g]) seen[p] = 1

        for (p in seen) {
            w = wins[g][p]+ 0
            l = losses[g][p]+ 0
            d = draws[g][p]+ 0
            ratio = (l == 0) ? w : w/l
            data[i,"p"]=p
            data[i,"w"]=w
            data[i,"l"]=l
            data[i,"d"]=d
            data[i,"ratio"]=ratio
            i=i+1
            
        }
        if(sort_by == "wins"){
            for(j=0;j<i;j++){
                key[j]=data[j,"w"]
            }
        }
        else if(sort_by=="losses"){
            for(j=0;j<i;j++){
                key[j]=data[j,"l"]
            }
        }
        else if (sort_by == "ratio"){
            for(j=0;j<i;j++){
                key[j]=data[j,"ratio"]
            }
        }
        asorti(key,idx,"@val_num_desc")
        for(j=1;j<=i;j++){
            k=idx[j]
            printf "%-20s %-8d %-8d %-8d %-8.2f\n", data[k,"p"], data[k,"w"],data[k,"l"],data[k,"d"],data[k,"ratio"]
        }

        
        
        print ""
    }
}
' "$HISTORY"
echo -e "${RESET}"