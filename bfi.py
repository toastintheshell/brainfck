#!/usr/bin/python    

""" Python BrainFuck interpreter """

import sys

print sys.argv

commands = ""
turing = [0]


if len(sys.argv) > 1:
    commands = sys.argv[1]

if commands:
    print commands

for i in commands:
    if i == "+":
        print i
    elif i == "-":
        print i
    elif i == ">":
        print i
    elif i == "<":
        print i
    elif i == "[":
        print i
    elif i == "]":
        print i
    elif i == ".":
        print i
    elif i == ",":
        print i
    else: 
        print "what's this "+i+" of which you speak?"

print "success!"
