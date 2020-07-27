# @param s string字符串
# @return string字符串
#
class Solution:
    def change(s ):
        result=[]
        num=0
        for i in s:
            if i=='a':
                num=num+1;
            else:
                if i!='"':
                    result.append(i)
        result.append('a'*num)
        a=''.join(result)
        print(a)
        return a
class Solution2:     #这是解决方案2
    def change(s ):
        news = [i for i in s]
        news.sort(key=lambda x:x=='a')
        s = ''.join(news)
        return s
if __name__ =="__main__":
    s=input()
    result=Solution2.change(s)
    print(result)
