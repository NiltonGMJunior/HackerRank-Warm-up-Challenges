def repeatedString(s, n):
    return s.count('a')*(n//len(s)) + s[:n % len(s)].count('a')

if __name__ == '__main__':
    print(repeatedString('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq',549382313570))
