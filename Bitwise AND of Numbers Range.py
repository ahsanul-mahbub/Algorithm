left = int(input())
right = int(input())
result  = 0
for i in range(32):
    if left & (1<<i) == 0:
        continue
    else:
        twos_power = 1 << (i+1)
        remainder = left % twos_power
        dif = twos_power - remainder
        range_ = right - left
        if range_ < dif:
            result = result | (1 <<i)
print(result)
