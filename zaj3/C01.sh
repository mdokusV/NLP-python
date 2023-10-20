#!/bin/bash
read input
sortednumbers=$(echo $input | tr ' ' '\n' | sort -n -r -u)
echo $sortednumbers