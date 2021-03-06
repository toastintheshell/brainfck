#!/usr/bin/python    

"""     A slightly malfunctional Python BrainFuck interpreter
    Takes 1 argument, brainfuck code in double quotes
    The following bf commands appear fully functional: +-<>.,
    The following bf commands are partially implemented but don't work yet: []
    """

import sys

print sys.argv

commands = ""
turing = [0]
pos = 0
x = 0 # ord of raw char in
iter = 0
nest_level = 0

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
        # changed for loop to while, now use nest_level value to allow nesting
        #
        # "if the byte at the data pointer is zero, then instead of moving the 
        # instruction pointer forward to the next command, jump it forward to 
        # the command after the matching ] command."
        #                                                           -wikipedia
        if turing[pos] == 0:
            nest_level += 1
        else:
            for i in commands[pos+1:]:
                if nest_level != 0:
                    if i != "]":
                        nest_level -= 1
                else: 
                    break
        print commands[iter]
        print "nest level: "+str(nest_level)
    elif commands[iter] == "]":
        # similar to [ of course
        #
        # "if the byte at the data pointer is nonzero, then instead of moving 
        # the instruction pointer forward to the next command, jump it back to 
        # the command after the matching [ command."
        #                                                           -wikipedia
        for i in reversed(commands[:pos]):
            if nest_level == 0:
                if turing[pos] != 0:
                    break
            elif i == "[":
                nest_level -= 1
            else: 
                iter -= 1
            #print commands.rfind("[", 0, pos)
            print "nest level: "+str(nest_level)
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
    print "iteration: "+str(iter)

print "success!"
