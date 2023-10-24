#!/bin/bash
cat ./C02.csv | cut -d" " -f 3 | sort -r | head -n 1