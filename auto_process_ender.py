import argparse
import psutil
import subprocess
import os
import time 

parser = argparse.ArgumentParser(description='A tool to repeatedly kill a process with a defined time interval.')
parser.add_argument('-pname', required=True, metavar='process name', type=str,
                    help='The name of the process to kill.')
parser.add_argument('--restart', action='store_true', 
                    help='The process will be restarted after killing.')
parser.add_argument('-interval', metavar='repeat interval', type=int,
                    help='The number of milliseconds to wait before killing the process again.')
args = parser.parse_args()

CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008

PROCESS_TO_KILL_NAME = args.pname
PROCESS_RESTART = args.restart
PROCESS_INTERVAL = args.interval or 0

if (PROCESS_INTERVAL % 2 != 0):
    PROCESS_INTERVAL += 1
    if PROCESS_INTERVAL < 0:
        PROCESS_INTERVAL = 0
PROCESS_INTERVAL /= 1000

while True:
    dict_pids = {
        p.info["pid"]: p.info["name"]
        for p in psutil.process_iter(attrs=["pid", "name"])
    }

    killed = False

    for pid in dict_pids:
        #print (pid, dict_pids[pid])
        if dict_pids[pid] == PROCESS_TO_KILL_NAME:
            os.system("taskkill /F /PID " + str(pid))
            killed = True

    if killed and PROCESS_RESTART:
        subprocess.Popen(PROCESS_TO_KILL_NAME, 
            creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    if PROCESS_INTERVAL == 0:
        break
    time.sleep(PROCESS_INTERVAL)
