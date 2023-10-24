#!/bin/bash
cat ./C06.txt | sed 's/[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]/X/g' > ./C06_X.txt
