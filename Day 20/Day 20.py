input_file = 'Day 20\\Input.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

ips = []
for line in lines:
    ip = []
    lower = int(line.split('-')[0])
    upper = int(line.split('-')[1])
    ip.append(lower)
    ip.append(upper)
    ips.append(ip)

ip_list = sorted(ips)

def min_ip(ips):
    ip = 0
    i = 0
    while ip < 2**32:
        lower = ips[i][0]
        upper = ips[i][1]
        if ip < lower:
            return lower - 1
        else:
            ip = upper + 1
            i += 1

def check_ip(i, ips):
    for lower, upper in ips:
        if lower <= i <= upper:
            break
    else:
        if i < 2**32:
            return True
    return False

def count_ips(ips):
    total = 0
    poss = [ip[1] + 1 for ip in ips]
    good = [i for i in poss if check_ip(i, ips)]
    for ip in good:
        while check_ip(ip, ips):
            total += 1
            ip += 1
    return total

print("Part 1: " + str(min_ip(ip_list))) # Correct!
print("Part 2: " + str(count_ips(ip_list))) # Correct!