#!/bin/bash
seq $(wc -l < ./C07.txt) -1 1 | paste -d' ' - ./C07.txt | tac
