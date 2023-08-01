def check_sets(elemets, N, output):
    for i in range(len(elemets)-1):
        for j in range(i+1,len(elemets)):
            if sum(elemets[i:j+1])==N:
                output+=1
    return output

def count_sets(N):
    output = 0
    elemets = []
    if N%2!=0:
        output+=1 #for odd one set is always ther for itself
    for i in range(1,N//2+2,2):
        elemets.append(i)
    print(check_sets(elemets,N,output))

count_sets(9)
count_sets(8)
count_sets(13)
count_sets(2)