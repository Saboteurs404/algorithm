'''
正则匹配邮箱
'''

import re
email_list = ["test01@163.com", "text02@153.com", ".test03g@qq.com", "test04@gmail.com"]

for email in email_list:
    ret = re.match("[\w]{4,20}@(.*)\.com$", email)
    if ret:
        print("%s 是符合规定的邮件地址， 匹配后结果是：%s" %(email, ret.group()))
    else:
        print("%s 不符合要求" %email)