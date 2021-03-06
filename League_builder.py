"""
TreeHouse Project 2
League Builder
Ryan Daigle
Attempting an exceeds standards grade.
"""
import csv

def create_team_file(stuff, file_name):
    """
    Creates a file from the parameter file_name and writes to the file the value of
    stuff to create an evenly divided set of teams with equal experience.
    """
    #create the the file
    with open(file_name, "a") as file:
        for i in stuff:           
            for item in i:
                # creates the team
                if i.index(item) == 0:
                    file.write("-" * 30)
                    file.write("\n")
                    file.write(item)
                    file.write( "\n")
                    file.write("-" * 30)
                    file.write( "\n")
                else:
                    # writes the players to the team
                    for j in item:
                        file.write(j)
                        if item.index(j) == 3:
                            pass
                        else:
                            file.write(", ")
                file.write("\n")

def read_csv(thing):
    """
    Opens and displays thing a csv files contents by row and returns them as one
    list of lists.
    """
    with open(thing, newline='') as csvfile:
        
        csv_file = csv.reader(csvfile, delimiter=',')
        rows = list(csv_file)
        rows.pop(0)

        return rows
                 
def show_file(thing):
    """
    Opens and prints the value from the thing parameter in
    string form line by line
    """
    with open(thing, "r") as file:
        for line in file:
            print(line)

def team_create(rows):
    """
    Creates teams and assigns players to those teams.
    takes a list of rows from a csv file and reads it.
    """
    # initiates variables
    experienced = []
    inexperienced = []
    dragons= ['Dragons']
    raptors = ['Raptors']
    sharks = ['Sharks']
    teams = [sharks, dragons, raptors]
    
    # divides players evenly into teams
    for row in rows:
        if "YES" in row:
            experienced.append(row)
        elif 'NO' in row:
            inexperienced.append(row)
        else:
            pass
    # pops 3 experienced and inexperienced players and adds them to the current team.
    for team in teams:
        i = 0
        for i in range(0,3):
            i += 1
            team.append(experienced.pop(0))
            team.append(inexperienced.pop(0))
    
    return dragons, raptors, sharks

def create_guardians_letter(info):
    """
    Creates letters send to guardians.
    """
    team = ''
    player = ''
    guardian = ''
    for i in info:
        for item in i:
            if i.index(item) == 0:
                team = item
            else:
                for j in item:
                    if item.index(j) == 0:
                        orig_player = j
                        j = list(j)
                        j[j.index(' ')] = '_'
                        player = ''.join(j) + '.txt'
                    elif item.index(j) == 3:
                        guardian = j
                to_write = ("Dear {}, your child {} will be on the {} team. "
                                  "The first practice will be on 11/15/2018 "
                                  "at 6:00 PM EST.".format(guardian, orig_player, team))
                with open(player, "a") as file:
                    file.write(to_write)                        
                            
if __name__ == "__main__":
    TEAMS = team_create(read_csv("soccer_players.csv"))
    create_team_file(TEAMS,"teams.txt")
    create_guardians_letter(TEAMS)
    
