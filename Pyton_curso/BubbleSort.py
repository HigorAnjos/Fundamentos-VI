
def bubbleSort(vetor):
    for num in range(len(vetor)-1,0,-1):
        for i in range(num):
            if ( vetor[i]>vetor[i+1] ):
                aux = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = aux

vetor = [54, 26, 93, 17, 77, 31, 44, 55, 20]

bubbleSort(vetor)
print(vetor)

