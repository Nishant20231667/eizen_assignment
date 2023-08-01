def minimum_travel_T(N, M, A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    if B[0] < A[0]:
        return -1
    else:
        i, j = 1, 1
        T = 1
        source = M - 1
        max_time = -1

        while i < N:
            while B[j] < A[i]:
                i += 1
                T += 2
                if T > max_time:
                    max_time = T
            j += 1
            i += 1
            T = 1
            if T > max_time:
                max_time = T

            source -= 1

            if j == M and i != N:
                if source >= (N - i):
                    max_time += 1
                    break
                else:
                    source = M
                    max_time += 1
                    if source >= N - i:
                        max_time += 1
                        break
                    else:
                        k = ((N - i) // source) + ((N - i) % source != 0)
                        max_time += 2 * k - 1

        if T > max_time:
            max_time = T

        return max_time


# Example usage 1:
N = 4
M = 3
A = [2, 1, 2, 6]
B = [5, 6, 5]
print(minimum_travel_T(N,M,A,B))
# Example usage 2:
N = 4
M = 3
A = [8, 1, 6, 9]
B = [7, 3, 2]
print(minimum_travel_T(N,M,A,B))
