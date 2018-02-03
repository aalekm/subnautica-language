#!/usr/bin/env python3
import sys
import os.path

for file in os.listdir("./untouched"):
	f = open("/".join([".", "untouched", file]), "r")
	sequences = f.read()
	f.close()
	utf = bytes(sequences, "utf-8").decode("unicode_escape")

	out = open("/".join([".", "utf-8", file]), "w", encoding="utf8")
	out.write(utf)
	out.close()