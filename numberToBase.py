VALUES = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def numberToBase(num,fromB = 10,toB = 10):
    '''Converts a number inputed as a string from one base to another
    Arguments:
    > num -- string
    > fromB, base to convert from -- int [2,36]
    > toB, base to convert to -- int [2,36]
    returns:
    - string
    '''
    #We make sure that the bases are integers and num is a string
    fromB = int(fromB)
    toB = int(toB)
    num = str(num)
    #We make sure that the bases are in between 2 and 36
    assert fromB >= 2 and fromB <= 36
    assert toB >= 2 and toB <= 36
    #we convert num to decimal, making num an integer
    num = int(num, fromB)
    result = ''
    #If num is 0 or we want base 10, then we are done
    if num == 0 or toB == 10:
      result = str(num)
    else:
      #we convert num to a string in the target base and store it in result
      #We remove the negative sign and add it back at the end
      negative = False
      if num < 0:
          num = abs(num)
          negative = True
      while num > 0:
          result = VALUES[num%toB] + result
          num //= toB
      if negative:
          result = '-' + result
    
    return result
