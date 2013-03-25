#! /usr/bin/env python

def main():    # Don't leave the code in the global namespace, it runs slower
    import sys

    tokenizedInput = map(int, sys.stdin.read().split())
    testcases = tokenizedInput[0]

    alphabet = "bcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyzbcdefghijklmnopqrstuvwxyzb"

    for count in xrange(0,testcases):
        K = tokenizedInput[count+1]
        for x in reversed(xrange(0, K)):
            sys.stdout.write(alphabet[x])
            if (alphabet[x] == 'b'):
                sys.stdout.write('a')
        sys.stdout.write('\n')

main()
