import random as r

numbers = 6

def calc():
    lotto = []
    for x in range( numbers ):
        r = generate()
        if r not in lotto:
            print( "Calculating..." )
            lotto.append( r )
        else:
            lotto = []
            print( "Error occured!! Please don't use the array with less than six numbers!" )
    print( lotto )

def generate():
    return r.randrange( 1, 49 )

if __name__ == "__main__":
    print( "Welcome!" )
    print( "q = quit / lotto = generate 6 non-same numbers" )
    while True:
        _in = input( ">" )
        if _in == "lotto":
            calc()
        elif _in == "q":
            print( "Exiting..." )
            break
        else:
            print( _in, " is no function" )
