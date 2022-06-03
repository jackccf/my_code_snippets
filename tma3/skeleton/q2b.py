import timeit


def Fib(N):
    assert N >= 1
    if N == 1 or N == 2:
        return 1
    return Fib(N-1) + Fib(N-2)


if __name__ == '__main__':
    A = int(input('Enter the start of the series (A): '))
    B = int(input('Enter the end of the series (B): '))

    for i in range(A, B+1):
        print(f'{i:<5d} {Fib(i):<5d}', sep='\n')
