#!/bin/bash
cat ./C01.csv | tr ' ' '\n' | sort -n -r -u