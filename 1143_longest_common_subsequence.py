def longestCommonSubsequence(text1, text2):
    sub_sequence_size = 0
    for c in text1:
        print( f"{c} encontrado na posicao {text2.find(c)}")
    return 999

print(longestCommonSubsequence("AXXBXXCXXD","ABCD"))