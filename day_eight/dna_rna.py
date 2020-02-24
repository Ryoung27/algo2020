def DNAtoRNA(dna):
    answer = ''
    for i in dna:
        if i == 'T':
            answer += 'U'
        else:
            answer += i
    return answer
