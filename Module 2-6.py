import random

code1=''.join(str(random.randint(0,9)) for _ in range(3))
code2=''.join(str(random.randint(1,6)) for _ in range(4))

print("Random combined code:")
print(code1)
print(code2)