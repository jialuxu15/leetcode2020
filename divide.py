class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def Dividend(dividend:int,divisor:int)->int:
            
            if dividend<divisor:
                return dividend,0
            i=1
            dividend-=divisor
            while dividend>divisor:
                dividend-=divisor
                divisor+=divisor
                i=i+i
            return dividend,i

        
        def Divide(dividend: int, divisor: int) -> int:

            
            if dividend<divisor:
                return 0
             
            if divisor==1:
                return dividend

            if divisor==2:
                x=str(bin(dividend))
                return int(x[:-1],2)
            
            result=0
            while dividend>=divisor:
                dividend,i=Dividend(dividend,divisor)
                result+=i
            
            return result
            

        if dividend<0:
            if divisor>0:
                result= 0-Divide(0-dividend, divisor)
            else:
                result= Divide(0-dividend, 0-divisor)
        else:
            if divisor>0:
                result= Divide(dividend, divisor)
            else:
                result= 0-Divide(dividend, 0-divisor)
        
        if result<-2**31 or result>2**31-1:
            return 2**31-1
        else:
            return result
        
                    
a=Solution()
print(a.divide(2147483647,2147483647))


            
            
