n = int(input("Enter the number :"))
x = [True] * (n + 1)
p_n = []
p = 2

while p * p <= n:
    if x[p]:
        for i in range(p * p, n + 1, p):
            x[i] = False
    p += 1

for i in range(2, n + 1):
    if x[i]:
        p_n.append(i)

print(p_n)

___________________________________
SieveofEratosthenes notebook (https://colab.research.google.com/drive/1aFgAK4e1vb8T9yZ6-EBm8JV-T5Pp2f-q#scrollTo=KswfG2TSVumH)
Tutorial link (https://youtu.be/0T1-IjBM9jA?si=l60bZDJCkCkqlWrG)
