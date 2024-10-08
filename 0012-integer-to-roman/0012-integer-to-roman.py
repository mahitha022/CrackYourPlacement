class Solution:
    def intToRoman(self, num: int) -> str:
        d={1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        s=""
        for i in d:
            div=num//i
            rem=div*i
            
            if(rem>0):
                s+=d[i]*div
                num-=rem
            if(num==0):
                break
        return s