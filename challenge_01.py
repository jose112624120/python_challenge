TEXT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

URL = "http://www.pythonchallenge.com/pc/def/map.html"

def shiftby2(s):
    shifted = ord(s)
    if ('a' <= s) and (s <= 'z'):
        shifted += + 2
        if shifted > ord('z'):
            shifted =  ord('a') + shifted - ord('z') - 1
    return chr(shifted)
    
def main():
    print('main')
    mapped  = map(shiftby2,TEXT)
    mapped_str = ''.join([x for x in mapped])
    print(mapped_str)

    mapped  = map(shiftby2,"map")
    mapped_str = ''.join([x for x in mapped])
    print(mapped_str)
    print('next challenge:\n',URL.replace('map', mapped_str))
    print('other (more clever) solutions:\n',URL.replace('map', mapped_str).replace('pc','pcc')) 

if __name__ == '__main__':
    main()