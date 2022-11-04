def octets(bit_s):
    if len(bit_s)%4 != 0:
        bit_s = ''.join('0' for i in range(4-len(bit_s)%4)) + bit_s
    
    return bit_s
 
def comp2(bit_s):
    bit_s = str(bit_s)
    result = str(bit_s)
    if int(bit_s) != 0:
        bit_s = octets('0'+bit_s)
        inverse_s = ''.join(['1' if i == '0' else '0' for i in bit_s])
        dec = int(inverse_s,2)+1
        result = bin(dec)[2:]
    result = octets(result)
    result = ' '.join(result[i:i+4] for i in range(0, len(result), 4))
    print(result)
