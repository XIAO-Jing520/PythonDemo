import subprocess
import re
import platform


def find_all_ip():
    os_type = platform.system()
    ipstr = r'([0-9]{1,3}\.){3}[0-9]{1,3}'
    if os_type == "Darwin" or os_type == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        ip_pattern = re.compile('(inet %s)' % ipstr)
        if os_type == "Linux":
            ip_pattern = re.compile('(inet addr:%s)' % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, str(output)):
            ip = pattern.search(ipaddr.group())
            if ip.group() != "127.0.0.1":
                iplist.append(ip.group())
        return iplist
    elif os_type == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        output = output.decode('gbk')  # ！！！！匹配中文的时候，需要先将byte编码为gbk字符串，在进行匹配
        ip_pattern = re.compile(r"IPv4 地址 (\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        iplist = []
        for ipaddr in re.finditer(ip_pattern, output):
            ip = pattern.search(ipaddr.group())
            iplist.append(ip.group())
        return iplist


def find_all_mask():
    os_type = platform.system()
    ipstr = r'([0-9]{1,3}\.){3}[0-9]{1,3}'
    maskstr = r'0x([0-9a-f]{8})'
    if os_type == "Darwin" or os_type == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        mask_pattern = re.compile(r'(netmask %s)' % maskstr)
        pattern = re.compile(maskstr)
        if os_type == "Linux":
            mask_pattern = re.compile(r'Mask:%s' % ipstr)
            pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(str(output)):
            mask = pattern.search(maskaddr.group())
            if mask.group() != '0xff000000' and mask.group() != '255.0.0.0':
                masklist.append(mask.group())
        return masklist
    elif os_type == "Windows":
        ipconfig_process = subprocess.Popen("ipconfig", stdout=subprocess.PIPE)
        output = ipconfig_process.stdout.read()
        output = output.decode('gbk')  # ！！！！匹配中文的时候，需要先将byte编码为gbk字符串，在进行匹配
        mask_pattern = re.compile(r"子网掩码  (\. )*: %s" % ipstr)
        pattern = re.compile(ipstr)
        masklist = []
        for maskaddr in mask_pattern.finditer(output):
            mask = pattern.search(maskaddr.group())
            masklist.append(mask.group())
        return masklist


def get_broad_addr(ipstr, maskstr):
    iptokens = map(int, ipstr.split("."))
    masktokens = map(int, maskstr.split("."))
    broadlist = []
    iptokens = list(iptokens)
    masktokens = list(masktokens)
    for i in range(len(iptokens)):
        ip = iptokens[i]
        mask = masktokens[i]
        broad = ip & mask | (~mask & 255)
        broadlist.append(broad)
    return '.'.join(map(str, broadlist))


def find_all_broad():
    os_type = platform.system()
    ipstr = '([0-9]{1,3}\.){3}[0-9]{1,3}'
    if os_type == "Darwin" or os_type == "Linux":
        ipconfig_process = subprocess.Popen("ifconfig", stdout=subprocess.PIPE)
        output = (ipconfig_process.stdout.read())
        broad_pattern = re.compile('(broadcast %s)' % ipstr)
        if os_type == "Linux":
            broad_pattern = re.compile(r'Bcast:%s' % ipstr)
        pattern = re.compile(ipstr)
        broadlist = []
        for broadaddr in broad_pattern.finditer(str(output)):
            broad = pattern.search(broadaddr.group())
            broadlist.append(broad.group())
        return broadlist
    elif os_type == "Windows":
        iplist = find_all_ip(os_type)
        masklist = find_all_mask(os_type)
        broadlist = []
        for i in range(len(iplist)):
            broadlist.append(get_broad_addr(iplist[i], masklist[i]))
        return broadlist
