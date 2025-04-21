print("Welcome to the fact finder game🧿🧿🧿🧿")
print("Tell me a number and I will Find its Factors")
num=int(input("🔢🔢🔢🔢🔢Enter a number: "))
print(f"\n Finding Numbers of {num}......🧿🧿🧿🧿🧿🧿🧿🧿🧿🧿🧿🧿")
factors=[ ]
for i in range(1,num+1):
    if num% i == 0:
        factors.append(i)
        print("{} is a factor".format(i))
print(f"\n All Factors of {num} are {factors} ")