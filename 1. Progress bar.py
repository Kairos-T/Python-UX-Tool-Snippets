#import sys 

progress = n / length * 100
        sys.stdout.write('\r')
        sys.stdout.write("[%-100s] %d%%" % ('=' * int(progress), progress))
        sys.stdout.flush() 
