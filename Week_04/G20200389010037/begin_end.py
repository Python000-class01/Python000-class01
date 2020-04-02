import ansible
import paramiko
import time
host = "169.254.163.93"
user='root'
passw0rd='Wo123456'
  # 创建SSH对象
ssh = paramiko.SSHClient()
 # 连接服务器
ssh_fd = ssh
# 允许连接不在know_hosts文件中的主机
ssh_fd.set_missing_host_key_policy(paramiko.AutoAddPolicy())   
#连接
ssh_fd.connect(hostname=host, username=user, password=passw0rd)
timebegining = time.time()
cmd = input("input your request")
if cmd= "ansible  "/etc"*"/init.d"*"/nginx" start|restart":#逐层进或者直接复制路径进
    nginx.exe.start()
elif cmd= "/etc"*"/init.d"*"/nginx" stop|restart":
    print("nginx: [emerg] still could not bind()")
if time.time()-timebegining>=60:
    ssh_fd.close()
# shell     /etc/init.d/nginx   start|stop|restart|reload|status
