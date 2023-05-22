if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # i + j + k != n
    # 0 <= i <= x
    # 0 <= j <= y
    # 0 <= k <= z
    total_arr = [] # cách viết đầy đủ
    for i in range(0,(x+1),1):
        for j in range(0,(y+1),1):
            for k in range(0,(z+1),1):
                if(i+j+k) != n:
                    total_arr.append([i,j,k])

    # Cách viets rút gọn
    total_arr2 = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

    print(total_arr2)