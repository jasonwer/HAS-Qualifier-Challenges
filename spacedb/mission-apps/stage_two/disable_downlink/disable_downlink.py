#!/usr/bin/env python3

# What needs to be done:

# Prints flag to the log on reboot.

import argparse
import subprocess
import app_api
import sys
import time
import toml
import random
import pickle
import csv
from datetime import datetime, timedelta
from app_api import CH_CONF_PATH as CONFIG_PATH

def main():

    logger = "disable_downlink "   
       
    parser = argparse.ArgumentParser()
    
    #Add argument for csv file list

    parser.add_argument('--config', '-c', nargs=1)
    
    args = parser.parse_args()
    
    if args.config is not None:
        global SERVICES
        SERVICES = app_api.Services(args.config[0])
    else:
        SERVICES = app_api.Services(CONFIG_PATH)

    print(f"{logger} warn: Downlink not running")
    sys.stdout.flush()
    # print(f"{logger} warn: Beginning downlink...")

    run_list = ['/challenge/mission-apps/stage_two/win_check/win_check.py', '--lose']
    p = subprocess.Popen(run_list)
    p.communicate()
    print('')

if __name__ == "__main__":
    main()