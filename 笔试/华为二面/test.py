'''

题目描述
Solo小学一年级的时候做数学题很莫名奇妙，经常把算术表达式加上很多空格（如：7+ 31    -2），
让老师很是头大，于是老师决定雇用你编写一个程序来独立计算Solo的答案。Can you help the teacher?

解答要求
时间限制：5000ms, 内存限制：100MB
输入
输入只有一行，即一个长度不超过100的字符串S，表示Solo的算术表达式，且S只包含数字和”+”、”-”两种运算符，以及Solo加上的一大堆空格（我们保证输入都是合法的）。
注意：S中不一定包含运算符，且我们保证S中不会出现大于100000的数。

输出
输出表达式的运算结果。

样例
输入样例 1 复制

1+2 + 3 +   4
输出样例 1

10
提示样例 1
eval

提示
'''
class Solution:
    def dispose(self, s):
        s = s.replace(' ', '')
        partition = []
        temp = ''
        sum = 0
        for item in s:
            if item == '+' or item == '-':
                partition.append(temp)
                partition.append(item)
                temp = ''
            else:
                temp += item
        partition.append(temp)

        # print(partition)
        while partition:
            temp = partition.pop(0)
            if temp == '+':
                sum += int(partition.pop(0))
            elif temp == '-':
                sum -= int(partition.pop(0))
            else:
                sum = int(temp)

        return sum


if __name__ == '__main__':
    s = '1+2 + 3 +   4   - 6'
    s2 = '10'
    result = Solution().dispose(s)
    print(result)



