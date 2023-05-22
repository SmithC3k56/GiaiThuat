if __name__ == '__main__':
    N = int(input())
    result = []
    print_result = []
    for _ in range(N):
        inparr = input().split(' ')
        cmd = inparr[0]
        integer_array = [int(value) for value in inparr[1:]]
        if cmd == 'insert':

            result.insert(*integer_array)
        elif cmd == 'remove':
            result.remove(integer_array[0])
        elif cmd == 'append':
            result.append(integer_array[0])
        elif cmd == 'sort':
            result.sort()
        elif cmd == 'pop':
            result.pop()
        elif cmd == 'reverse':
            result.reverse()
        elif cmd == 'print':
            print(result)
