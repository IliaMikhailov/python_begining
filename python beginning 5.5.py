with open('text.txt', 'w') as f:
    f.write(input('введите строку из чисел разделённых пробелом '))
with open('text.txt', 'r') as f:
    user_str = f.read().split()
    for i in range(len(user_str)):
        user_str[i] = int(user_str[i])
print(sum(user_str))
