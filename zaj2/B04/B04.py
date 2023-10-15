#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import os
import re

DIR = os.path.dirname(__file__)


def join_path(filename: str) -> str:
    return os.path.join(DIR, filename)


with open(join_path("text.txt"), "r", newline="") as file:
    text = file.read()

    # Wyra¿enie regularne do wyszukiwania adresów e-mail
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # Wyszukanie adresów e-mail w tek¶cie
    emails = re.findall(email_pattern, text)

print(emails)
