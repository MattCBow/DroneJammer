#!/bin/bash

echo "Putting ALFA (wlx00c0ca82925c) into Monitor Mode"


ifconfig wlx00c0ca82925c down
iwconfig wlx00c0ca82925c mode monitor
ifconfig wlx00c0ca82925c up
