class Solution:
    def numberToWords(self, num: int) -> str:
        d={1000000000:" Billion", 1000000:" Million", 1000:" Thousand", 100:" Hundred", 90:" Ninety", 80:" Eighty", 70: " Seventy", 60:" Sixty", 50:" Fifty", 40:" Forty", 30:" Thirty", 20:" Twenty", 19:" Nineteen", 18:" Eighteen", 17:" Seventeen",  16:" Sixteen", 15:" Fifteen", 14:" Fourteen", 13:" Thirteen",  12:" Twelve", 11:" Eleven", 10:" Ten", 9:" Nine", 8:" Eight", 7: " Seven", 6:" Six", 5:" Five", 4:" Four", 3:" Three", 2:" Two", 1:" One", 0:""}
        
        def help(num):
            if(num<20):
                return d[num]
            elif(num<100):
                x=(num//10)*10
                return d[x]+d[num%10]
            elif(num<1000):
                return d[num//100]+d[100]+help(num%100)
            
            else:
                for i in range(3,0,-1):
                    if(num>=1000**i):
                        return help(num//(1000**i)) + d[1000**i] + help(num%(1000**i))
        
        if(num==0):
            return "Zero"
        return help(num).lstrip()




