
def mergeAlternately(world1, world2):
    
    world1_size = len(world1)
    world2_size = len(world2)
    merged_string = ''

    i = 0
    j = 0
    k = 0

    while i < (world1_size + world2_size):

        if j < world1_size:
            merged_string = merged_string + world1[j]
            j = j + 1

        if k < world2_size:
            merged_string = merged_string + world2[k]
            k = k + 1

        i = i + 1

    return merged_string

print(mergeAlternately('aaa',''))
