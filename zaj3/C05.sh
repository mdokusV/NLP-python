#!/bin/bash
cat ./C05.txt | grep -o -E "(cz)|(sz)" | wc -l