if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # 2<= n <= 10
    # -100 <= A[i] <=100
    min = -100
    rs = [min, min]  # rs luôn là phần tử nhỏ nhất trong mảng
    for i in arr:
        if i > rs[0]:
            rs[1] = rs[0]
            rs[0] = i

        else:
            if i > rs[1] and i < rs[0]:
                rs[1] = i

    print(rs[1])
