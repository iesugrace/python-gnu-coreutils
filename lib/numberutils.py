import re

def convertHumanNumber(inNumber):
    """
    Convert number of these units to bytes:
    b   : 512 
    kB  : 1000
    K   : 1024
    mB  : 1000*1000
    m   : 1024*1024
    MB  : 1000*1000
    M   : 1024*1024
    GB  : 1000*1000*1000
    G   : 1024*1024*1024
    TB  : 1000*1000*1000*1000
    T   : 1024*1024*1024*1024
    PB  : 1000*1000*1000*1000*1000
    P   : 1024*1024*1024*1024*1024
    EB  : 1000*1000*1000*1000*1000*1000
    E   : 1024*1024*1024*1024*1024*1024
    ZB  : 1000*1000*1000*1000*1000*1000*1000
    Z   : 1024*1024*1024*1024*1024*1024*1024
    YB  : 1000*1000*1000*1000*1000*1000*1000*1000
    Y   : 1024*1024*1024*1024*1024*1024*1024*1024

    inNumber is of one of these forms:
    123, 123b, 123M, 1G

    """
    mapping = {
        'b'  : 512 ,
        'kB' : 1000,
        'K'  : 1024,
        'mB' : 1000*1000,   # redundant
        'm'  : 1024*1024,   # redundant
        'MB' : 1000*1000,
        'M'  : 1024*1024,
        'GB' : 1000*1000*1000,
        'G'  : 1024*1024*1024,
        'TB' : 1000*1000*1000*1000,
        'T'  : 1024*1024*1024*1024,
        'PB' : 1000*1000*1000*1000*1000,
        'P'  : 1024*1024*1024*1024*1024,
        'EB' : 1000*1000*1000*1000*1000*1000,
        'E'  : 1024*1024*1024*1024*1024*1024,
        'ZB' : 1000*1000*1000*1000*1000*1000*1000,
        'Z'  : 1024*1024*1024*1024*1024*1024*1024,
        'YB' : 1000*1000*1000*1000*1000*1000*1000*1000,
        'Y'  : 1024*1024*1024*1024*1024*1024*1024*1024,
    }
    unit = re.sub('[0-9]+', '', inNumber)
    if unit:
        return mapping[unit]
    else:
        return inNumber
