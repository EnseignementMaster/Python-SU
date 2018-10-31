try:
    l = range('10')
except TypeError as e:
    print( 'TypeError')
except:
    print( 'mauvaise utilisation')