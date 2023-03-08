n=int(input("Entre el [1 - 100] cuantos son multiplos de: "))
for ran in range(1, 101):
    if ran%n==0:
        print(ran)

