fibo = [0,1]
while len(fibo)<20:
    fibo.append(fibo[len(fibo)-2] + fibo[len(fibo)-1])
    print(fibo[len(fibo)-1], end=' ')