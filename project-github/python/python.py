import random
l_w = "zxcvbnmlkjhgfdsaqwertyuiop"
u_w = l_w.upper()
number = "0123456789"
c = "!@#$%^&*()"
ch = l_w + u_w + number + c
passl = str.join(random.sample(ch , 8))
print(passl)