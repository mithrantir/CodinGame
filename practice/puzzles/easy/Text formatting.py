import sys
import math
import re

intext = input().strip().split('.')

outtext = ""
for s in intext:
    sentence = s.strip()
    if len(sentence) < 2:
        continue
    sentence = re.sub(r'\s{2,}', ' ', sentence)
    sentence = re.sub(r'\s?[^\s\w\d]\s?', lambda match: match.group().strip(), sentence)
    sentence = re.sub(r'[^\s\w\d]+', lambda match: match.group().strip()[0], sentence)
    sentence = re.sub(r'[^\s\w\d]', lambda match: match.group() + ' ', sentence)
    sentence = sentence.lower()
    outtext += sentence[0].upper() + sentence[1:]
    if intext.index(s) < len(intext)-1:
        outtext += '. '

print(outtext.strip())
