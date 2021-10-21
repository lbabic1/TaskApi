import requests
import json
import datetime
import os
import sys

from requests.api import options

today = datetime.datetime.utcnow()
r = requests.get('http://127.0.0.1:8000/player')
packages_json = r.json()

def datereturn(date):
    date = date.replace("T", " ").replace("Z", "")
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")


def LatestPull(file):
    f = open(file, "a")
    if os.path.getsize(file) != 0: 
        with open(file) as f:
            for line in f:
                pass
            last_line = line
        return datetime.datetime.strptime(last_line[-26:], "%Y-%m-%d %H:%M:%S.%f")
    else:
        return datetime.datetime.strptime("2000-10-10 10:20:36.1", "%Y-%m-%d %H:%M:%S.%f")

def ListOfPlayers():
    last_pull = LatestPull("ListOfPlayers.txt")
    f = open("ListOfPlayers.txt", "a")
    f.write("\n\n")
    for i in range(len(packages_json)):
        LastModified = datereturn(packages_json[i]['LastModified'])
        if LastModified > last_pull:
            f.write("\n" +json.dumps(packages_json[i], indent=2))
    f.write("\n-------------------------------\nLatest pull: " + str(today))
    f.close()
    return

def OnePlayer(id):
    last_pull = LatestPull("OnePlayer.txt")
    f = open("OnePlayer.txt", "a")
    for i in range(len(packages_json)):
        LastModified = datereturn(packages_json[i]['LastModified'])
        if (packages_json[i]['PlayerId']) == id:
            f.write("\n\n" + json.dumps(packages_json[i], indent=2) + "\n")
            f.write("-------------------------------\nLatest pull: " + str(today))
            return
    f.close()
    return

if __name__ == "__main__":
    print("Choose 1 for list of players, or 2 for specific player: ")
    input =  sys.stdin
    option = input.readline()
    option = int(option, 10)
    if option == 1:
        ListOfPlayers()
    elif option == 2:
        print("Please enter player's id: ")
        id = input.readline()
        OnePlayer(int(id, 10))
        
