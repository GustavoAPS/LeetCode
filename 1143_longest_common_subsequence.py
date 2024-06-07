

def longestCommonSubsequence(text1, text2):
      
    largest_sub_sequence_size = 0


    for x in range(0,len(text1)):
        
        current_text1 = text1[x:]
        current_text2 = text2
        current_largest_sub_sequence_size = 0

      

        for c in current_text1:
            if current_text2.find(c) != -1: #if the char does not exist, skip the char
                first_occurance = current_text2.find(c)
                print( f"{c} Found in pos {first_occurance} resulting substring {current_text2[ (first_occurance+1) :]} ")
                current_largest_sub_sequence_size = (current_largest_sub_sequence_size + 1)
                current_text2 = current_text2[ (first_occurance+1) :]

            if current_largest_sub_sequence_size > largest_sub_sequence_size:
                largest_sub_sequence_size = current_largest_sub_sequence_size
        print("----------")


    return largest_sub_sequence_size

print(f"the largest subsequence is: {longestCommonSubsequence('','')}")