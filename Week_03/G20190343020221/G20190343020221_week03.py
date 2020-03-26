from scapy_ping_one_new_v2 import scapy_ping_one
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import ipaddress,datetime,sys,pickle

def ping_scan(network,pnum):
	#多进程
	pool = ProcessPool(processes = int(pnum))
	#多线程
	# pool = ThreadPool(processes = 150)
	net = ipaddress.ip_network(network)

	result_obj_dict = {}

	for ip in net:
		#获取返回的对象
		result_obj = pool.apply_async(scapy_ping_one,args =(str(ip),))
		result_obj_dict[str(ip)] = result_obj

	pool.close()
	pool.join()

	active_ip = []

	for ip,obj in result_obj_dict.items():
#		print (obj.get())
		if obj.get()[1] == 1:
			active_ip.append(ip)
	return active_ip

if __name__ == '__main__':
	today = datetime.datetime.now()
	today_format = today.strftime('%Y-%m-%d_%H%M%S')
	file_name = ('{0}{1}{2}'.format('ping_scan_pickle_',today_format,'.pl'))

	active_ip = (ping_scan(sys.argv[1],sys.argv[2]))
        
	scan_file = open(file_name,'wb')
	pickle.dump(active_ip,scan_file)   #将结果存为pick文件
	scan_file.close()

	scanfile = open(file_name,'rb')
	scan_list = pickle.load(scanfile)
	print ('active host list: \n')
	for ip in scan_list:
		print (ip) 
