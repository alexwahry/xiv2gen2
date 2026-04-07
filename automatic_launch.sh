#!/bin/bash

# run xivlauncher (it should be in your $PATH, obviously)
nohup "xivlauncher-core" &> /dev/null &

# five seconds to cancel the game launch if, for example, you want to change the XIVLauncher settings.
sleep 5

# it tries to enter code thirty times, one attempt each second
for i in {1..30}; do 
  
  python3 "$(cd "$(dirname "$0")" && pwd)/main.py" 
  
  # if command above ends with code 0, break loop immediately
  if [ $? -eq 0 ]; then 
    break; 
  fi

  sleep 1;

done