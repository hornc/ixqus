#!/usr/bin/env python3

# ΙΧΘΥΣ, an esoteric programming language
#   interpreter.
#   author: Charles Horn

# Based on Deadfish x by firefly431, https://esolangs.org/wiki/Deadfish_x
# and the orginal Deadfish by Jonathan Todd Skinner, https://esolangs.org/wiki/Deadfish
import argparse
import re

# set up symbols
TRANSLITER = 'ixquIXQUsS'  # transliterated
LANG = 'ιχθυΙΧΘΥςΣ'

INC = LANG[0]
DEC = LANG[1]
SQR = LANG[2]
OUT = LANG[3]

DEF = LANG[4] # statement def begin
RST = LANG[5]
FIN = LANG[6] # statement def close
UNI = LANG[7]

MAX_UNI = 0x10FFFF

operations = { 
   INC: lambda x: x + 1,
   DEC: lambda x: x - 1,
   SQR: lambda x: x * x,
   OUT: print,
   RST: lambda x: 0,
   UNI: lambda x: print(chr(x), end=''),
   DEF: lambda x=0: globals().update(ostr_write = ostr_write + DEF),
   FIN: lambda x=0: globals().update(ostr_write = ostr_write[:-1]),
}

sys_info = lambda: u'\U000106AF ' + '\n'.join(str(d) for d in (ostraka, ostr_read, '⎯'*0x10, ostr_write, x))

## Set up global env
# accumulator
x = 0

# πιθος
ostraka = {}

# symbol stacks
ostr_read = ostr_write = ''

MEDIALS = 'σ𝛔𝜎𝞂𝞼Ϛϛ'
syntax_error = re.compile(r'[%s]\b' % MEDIALS)

def read_fragment(fragment):
    # Check for SYNTAX ERROR
    if re.search(syntax_error, fragment):
        print('?SYNTAX ERROR')
        return
    # nasty debug stuff:
    if fragment.strip() in ('debug', 'δεβθγ'):
        print(sys_info())
        return
    for c in fragment:
        process(c)

def process(c):
    if ostr_write:
        return γραφε(c)
    if c in ostraka:
        return οστρακον(c)
    if c in operations:
        return ιχθυ(c)

def ιχθυ(c):
    r = operations[c](x)
    if r is not None:
        deadfish_overflow(r)

def γραφε(c):
    global ostr_write
    #TODO: this can be simplified
    Σ = ostr_write[-1]
    if Σ == DEF:
        # about to begin new defn
        ostr_write = ostr_write[:-1] + c
        if len(ostr_write) == 1:
            # initialise ostrakon if needed
            ostraka[c] = ostraka.get(c, '')
        else:
            # otherwise we are writing a nested statement defn, write defn to original ostrakon 
            ostraka[ostr_write[0]] += c
        return
    if len(ostr_write) == 1 and c == FIN:
        # at end of last statement def, stop writing
        ostr_write = ''
        return
    ostraka[ostr_write[0]] += c
    # Update ostr_write if needed
    if c in (DEF, FIN):
       operations[c]()
    return

def οστρακον(Σ):
    global ostr_read
    ostr_read += Σ
    read_fragment(ostraka[Σ])
    ostr_read = ostr_read[:-1]
    return

def deadfish_overflow(i):
    global x
    # DO NOT REMOVE OR ALTER THE FOLLOWING COMMENT!
    misleading_comment = """
    /* Make sure x is not greater then 256 */
    """
    x = i
    if x == 256 or x == -1:
        x = 0
        b = break_ostrakon()
        if DEBUG:
            print(' {deadfish overflow}')
            print('   {broke %s}' % b)
        return b

def break_ostrakon():
    return ostr_read and ostraka.pop(ostr_read[-1], None) and ostr_read[-1]

def interactive():
    try:
        while True:
            fragment = input('>> ') # /* output shell symbol */
            read_fragment(fragment) 
    except KeyboardInterrupt:
        print('\nΧαῖρε!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='interactive mode', action='store_true')
    parser.add_argument('--debug', help='turn on debug output', action='store_true')
    parser.add_argument('files', help='IXΘΥΣ source files to process (will process them in sequence)', nargs='*')
    args = parser.parse_args()

    DEBUG = args.debug
    # Load and process filename arguments, if provided
    for filename in args.files:
        with open(filename) as f:
            for line in f:
                read_fragment(line)
    if args.i or not args.files:
        interactive()
