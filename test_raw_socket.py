import socket
import sys
'''
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
	print("raw_socket successfully created!")
except socket.error:
	print ('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
'''

''' ip 头部

    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |ver    | HLEN  |Type_of_Service|          Total_Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment_Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time_to_Live |    Protocol   |         Header_Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source_Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination_Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |	// 选项和填充字段是没有的
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''

# !!!!!! 注意这里需要改一下！！！！
ip_source = '10.0.2.15' #本机IP
ip_dest = '64.4.11.42'	#也可以用域名：socket.gethostbyname('www.microsoft.com')

#填写ip header
ip_version = 4			# ipv4
ip_HLEN = 5			# Header Length =5, 暗示无options部分
ip_Type_of_Service = 0			# 服务种类 为零表示没有特殊要求
ip_total_len = 0		# left for kernel to fill
ip_Identification = 22222			# fragment相关，随便写个
ip_frag_offset = 0		# fragment相关
ip_ttl = 255			# *nix下TTL一般是255
ip_protocol = socket.IPPROTO_TCP	# 表示后面接的是tcp数据
ip_checksum = 0			# left for kernel to fill
ip_saddr = socket.inet_pton(socket.AF_INET, ip_source)	# 两边的ip地址
ip_daddr = socket.inet_pton(socket.AF_INET, ip_dest)

ip_version_ihl = (ip_ver << 4) + ip_ihl	# 俩4-bit数据合并成一个字节

# 按上面描述的结构，构建ip header。python library docs里面有句话挺有意思：
# The form '!' is available for those poor souls who claim they can't
# remember whether network byte order is big-endian or little-endian.
ip_header = pack('!BBHHHBBH4s4s' , ip_ver_ihl, ip_dscp, ip_total_len, ip_id, ip_frag_offset, ip_ttl, ip_protocol, ip_checksum, ip_saddr, ip_daddr)