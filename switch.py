import json 
from os import listdir
from os.path import join, basename, isfile
from imghdr import what as isimg
from sys import exit, argv
from subprocess import run as run_cmd

DEF_DIR = 1

def get_dir(args): 
    if len(args) == 1:
        return DEF_DIR
    
    try:
        val = int(args[1])
    except:
        return DEF_DIR
    
    return val


def next_from(dir, curr_ind, items_len): 
    if curr_ind + dir == items_len: 
        return 0

    if curr_ind + dir == -1: 
        return iems_len -1 

    return curr_ind + dir
    

def set(img_path):
    open("xf")

if __name__ == "__main__": 

    direction = get_dir(argv)    

    CONFIG = "/home/nemanja/.config/wpps.json"
    with open(CONFIG, "r") as f:
        config = json.load(f)

    dir = config.get("path")
    current_path = config.get("current")
    current_name = basename(current_path)

    next = None
    images = [
        item 
        for item in listdir(dir) 
        if (path := join(dir, item)) and isfile(path) and isimg(path)
    ]
    for ind, img_name in enumerate(images):
        if img_name == current_name:
            next_ind = next_from(direction, ind, len(images))
            next = images[next_ind]

    full_path = join(dir, next)
    cmd = f"xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitoreDP-1/workspace0/last-image  --set {full_path}"

    run_cmd(cmd.split(" "))

    new_cfg = {
        "path": dir, 
        "current": full_path
    }

    with open(CONFIG, "w") as f:
        json.dump(new_cfg, f, indent=2)  

