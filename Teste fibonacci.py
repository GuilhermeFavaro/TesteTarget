
# fibonacci 

def seqfibonacci(x):
    if x == 0:
        return [0]
    elif x == 1:
        return [0, 1]
    else:
        fn = [0, 1]
        for i in range(2, x +1):
            fn.append(fn[i-1] + fn[i-2])
        return fn

def in_seqfibonacci(x):
    fn = seq_fibonacci(x)
    if x in fn:
        return True
    else:
        return False

x = int(input("Número para testar: "))

if in_seq_fibonacci(x):
    print(f"{x} faz parte da sequência.")
else:
    print(f"{x} não faz parte da sequência.")       