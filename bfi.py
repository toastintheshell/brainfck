#!/usr/bin/python    

""" Python BrainFuck interpreter """

import sys

print sys.argv

commands = ""
turing = [0]
pos = 0

if len(sys.argv) > 1:
    commands = sys.argv[1]

if commands:
    print commands

for i in commands:
    if i == "+":
        turing[pos] += 1
        print i
    elif i == "-":
        turing[pos] -= 1
        print i
    elif i == ">":
        if len(turing)-1 == pos:
            turing.append(0)
        pos += 1
        print i
    elif i == "<":
        if pos != 0:
            pos -= 1
        else:
            print "already at position 0"
        print i
    elif i == "[":
        print i
    elif i == "]":
        print i
    elif i == ".":
        print chr(turing[pos])
        print i
    elif i == ",":
        print i
    else: 
        print "what's this "+i+" of which you speak?"
    print turing
    print "position: "+str(pos)

print "success!"
