def get_ip_pre(ip):
    n1,n2,n3,n4=ip.split('.')
    return n1+'.'+n2+'.'+n3+'.'
def get_ip_list (ip1,ip2):
    last_num_list =range(int(ip1.split('.')[-1:][0]),int(ip2.split('.')[-1:][0])+1)
    iplist = [get_ip_pre(ip1)+str(i) for i in last_num_list]
    return iplist
