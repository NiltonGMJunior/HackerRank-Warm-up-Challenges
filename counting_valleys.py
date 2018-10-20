
def countingValleys(n, s):

    alt = 0
    valley_count = 0
    sea_level = True

    for step in s:
        if sea_level and step == 'D':
            valley_count += 1
        alt += 1*(step == 'U') - 1*(step == 'D')
        sea_level = (alt == 0)

    return valley_count

def main():

    n = 8
    s = 'UDDDUDUU'

    print(countingValleys(n, s))

    return

if __name__ == '__main__':
    main()
