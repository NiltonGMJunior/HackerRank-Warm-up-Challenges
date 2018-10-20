def sockMerchant(n, ar):

    socks = [sock for sock in ar]
    socks.sort()
    num_pairs = 0

    while True:
        if len(socks) < 2:
            break
        if socks[0] == socks[1]:
            num_pairs += 1
            socks = socks[2:]
        else:
            socks = socks[1:]

    return num_pairs

def main():

    ar = [1,2,1,2,1,3,2]
    n = len(ar)
    print(sockMerchant(n,ar))

    return

if __name__ == '__main__':
    main()
