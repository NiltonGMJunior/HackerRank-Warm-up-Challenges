def jumpingOnClouds(c):

    num_jumps = 0
    cloud = 0

    while True:
        try:
            if c[cloud + 2] == 0:
                cloud += 2
            else:
                cloud += 1
        except IndexError:
            try:
                if c[cloud + 1] == 0:
                    cloud += 1
            except IndexError:
                break
        num_jumps += 1
        if cloud == len(c):
            break

    return num_jumps


if __name__ == '__main__':
    print(jumpingOnClouds([0, 1, 0 , 0, 1, 0]))
