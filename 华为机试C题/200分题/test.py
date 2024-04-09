

# 定义将二进制位数组转换为十进制数的函数
def bits_to_num(bits):
    # 对二进制位数组进行遍历，每位的值乘以其对应的2的幂次求和得到十进制数
    return sum(val * (2 ** idx) for idx, val in enumerate(bits))

# 定义分配信道的函数
def allocate_channels(channels, requirement):
    # 从最高阶开始向下遍历，尝试分配信道以满足需求
    for i in reversed(range(len(channels))):
        # 如果当前阶信道数量足够，直接减去需求量
        if channels[i] >= requirement[i]:
            channels[i] -= requirement[i]
        else:
            # 如果当前阶信道数量不足以满足需求，需要判断是否可以通过低阶信道组合满足需求
            # 首先判断当前及更低阶信道总容量是否小于需求的总容量
            if bits_to_num(channels[:i + 1]) < bits_to_num(requirement[:i + 1]):
                # 如果低阶总容量不足，尝试从更高阶借用一个信道
                for j in range(i + 1, len(channels)):
                    if channels[j] > 0:
                        channels[j] -= 1
                        return True
                # 如果高阶也无法借用，说明无法满足当前需求，返回False
                return False
            else:
                # 如果当前及更低阶信道总容量足够，先尝试分配当前阶，不足部分由更低阶信道通过倍增补足
                channels[i] -= requirement[i]
                if i > 0:
                    # 将不足部分的需求通过倍增转移到下一低阶，即需求翻倍
                    channels[i - 1] += channels[i] * 2
                # 将当前阶信道数量清零，因为已尽可能分配
                channels[i] = 0
    # 如果所有需求都能满足，返回True
    return True

if __name__ == '__main__':
    # 用户输入最大信道阶数
    max_level = 5
    # 用户输入每种信道的数量，按阶数从小到大
    channel_counts = [10,5,0,1,3,2]
    # 用户输入单个用户需要的数据量
    data_need = 30
    # 将用户需求的数据量转换为二进制位数组，并反转以符合从低阶到高阶的顺序
    print(bin(data_need)) # 0b11110
    requirement_bits = list(map(int, str(bin(data_need))[2:]))[::-1]
    print(requirement_bits)
    users_served = 0  # 初始化能服务的用户数
    # 对超出需求位长度的高阶信道，直接累加其数量至能服务的用户数
    for i in range(len(requirement_bits), max_level + 1):
        users_served += channel_counts[i]
    # 初始化当前可用信道数组，长度与需求位相同
    current_channels = channel_counts[:len(requirement_bits)]
    while len(current_channels) < len(requirement_bits):
        # 如果当前可用信道数组长度不足，补零以匹配需求位长度
        current_channels.append(0)
    # 尝试分配信道直到不再能满足任何用户的需求
    while allocate_channels(current_channels, requirement_bits):
        users_served += 1  # 成功分配则用户数加一

    # 输出能服务的用户总数
    print(users_served)
