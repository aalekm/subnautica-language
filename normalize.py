#!/usr/bin/env python3
import sys
import os.path

if len(sys.argv) <= 2:
  print("Usage:\n\tnormalize.py <filename> <output filename>")
  print("Converts unicode escape sequences to normal characters.")
  sys.exit(0)

if not os.path.exists(sys.argv[1]):
  print("File", sys.argv[1], "does not exist.")
  sys.exit(1)

f = open(sys.argv[1], "r")
sequences = f.read()
f.close()
utf = bytes(sequences, "utf-8").decode("unicode_escape")

out = open(sys.argv[2], "w", encoding="utf8")
out.write(utf)
out.close()