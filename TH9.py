

class Solution:

    def Orderofpoker(x):
        def sushu(k):
            z=0
            for i in range(2,k//2+1):
                if k%i==0:
                    z=1   #k不是素数
                    break
            else:
                z=0
            return z
        x=x[1:-1]
        num=len(x)
        print(num)
        a=""
        if num==2 or num==4 or num==6:
            a=x
        else:
            for k in range(num//2,3,-1):
                su=sushu(k)
                if su==1:
                    a+=x[-2:]
                    x=x[:-2]
                else:
                    a+=x[:2]
                    x=x[2:]
            a+=x
        return a
if __name__ == "__main__":
    input_number=input("please input:")
    a=Solution.Orderofpoker(input_number)
    print(a)
