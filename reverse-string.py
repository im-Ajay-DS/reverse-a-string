class Solution:
     def reverseWord(self, str: str) -> str:
        reversed_list=[]
        for i in range(len(s)-1,-1,-1):
            reversed_list.append(s[i])
        reversed_string=''.join(reversed_list)
        return reversed_string
