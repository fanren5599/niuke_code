#
#
# @param n int整型
# @param num int整型一维数组
# @return int整型
#
class Solution:
    def getMaxLength(self , n , num ):
        flag=0
        flag2=0
        result=0
        temp=0
        for i in range(0,n-1):
            if flag==0:
                if num[i]<num[i+1]:
                    temp+=1
                else:
                    if num[i]>num[i+1]:
                        temp+=1
                        flag=1
                        flag2=1
                    else:
                        temp=0
                        flag=0
            else:
                if num[i]>num[i+1]:
                    temp+=1
                    flag2=1
                else:
                    result=temp if temp>result else result
                    temp=1 if num[i]<num[i+1] else 0
                    flag=0
                    flag2=0
        if flag2==1:
            result=temp if temp>result else result
        result=result+1 if flag2==1 or result!=0 else 0
        return result
