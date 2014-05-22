#!/usr/bin/python    

"""     A 75% FULLY functional Python BrainFuck interpreter
    Takes 1 argument, brainfuck code in double quotes
    The following bf commands appear fully functional: +-<>.,
    The following bf commands are incomplete: []
    """

import sys

print sys.argv

commands = ""
turing = [0]
pos = 0
x = 0
iter = 0

if len(sys.argv) > 1:
    commands = sys.argv[1]

if commands:
    print commands

while iter < len(commands):
#for i in commands:
    if commands[iter] == "+":
        turing[pos] += 1
        print commands[iter]
    elif commands[iter] == "-":
        turing[pos] -= 1
        print commands[iter]
    elif commands[iter] == ">":
        if len(turing)-1 == pos:
            turing.append(0)
        pos += 1
        print commands[iter]
    elif commands[iter] == "<":
        if pos != 0:
            pos -= 1
        else:
            print "already at position 0"
        print commands[iter]
    elif commands[iter] == "[":
        # this is a tough one, might change main for loop to while
        print commands[iter]
    elif commands[iter] == "]":
        # similar to [ of course
        print commands[iter]
    elif commands[iter] == ".":
        if turing[pos] >= 0:
            print chr(turing[pos])
        else:
            print "cannot display negative number as char"
        print commands[iter]
    elif commands[iter] == ",":
        # type a char and press enter, may fix for direct from stdin later.
        x = ord(raw_input())
        turing[pos] = x
        print commands[iter]
    else: 
        print "what's this "+commands[iter]+" of which you speak?"
    print turing
    print "position: "+str(pos)
    iter += 1

print "success!"
