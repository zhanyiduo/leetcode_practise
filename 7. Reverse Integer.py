'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
def reverse(x):
    num = 0
    ini = 0

    if x < 0:
        x = -x
        sign = -1
    else:
        sign = 1
    for i in range(9,-1,-1):
        if (x - (10**i)) >= 0:
            ini = i
            break
    for j in range(ini,-1,-1):
        num += int(x / (10**j)) * (10**(ini-j))
        x -= int(x / (10**j)) * (10**j)

    if (sign*num > (2 ** 31 - 1)) | (sign*num < -2 ** 31):
        return 0
    else:
        return sign*num


if __name__ == "__main__":
    print(reverse(x=1534236469))
