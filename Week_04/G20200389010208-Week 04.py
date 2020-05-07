import sys
import paramiko

def ssh_connect(hostname, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, 22, username, password)
        return ssh
    except Exception as e:
        print('ssh %s@%s: %s' % (username, hostname, e))
        exit()

def nginx_stop(ipAddress, username):
    cmd = """ansible %s -u %s -m shell -a 'ps x|grep java|grep -v grep|cut -d " " -f 1|xargs kill -9'""" \
          % (ipAddress, username)
    ssh = ssh_connect()
    stdin, stdout, stderr = ssh_exec_command(ssh, cmd)

    if len(stderr.readlines()) != 0:
        print('Fail to stop！')
        sys.exit(0)
    else:
        print('Success to stop!')
    print([line for line in stdout.readlines()])

    ssh.close()

def nginx_start(ipAddress, username, command, ssh_host, ssh_user, ssh_pwd):
    cmd = "ansible %s -u %s -m shell -a 'source ~/.bash_profile && cd $BIN_HOME && sh %s'" \
              % (ipAddress, username, command)
    ssh = ssh_connect(ssh_host, ssh_user, ssh_pwd)
    stdin, stdout, stderr = ssh_exec_command(sshd, cmd)

    if len(stderr.readlines()) != 0:
        print('Fail to start!')
        sys.exit(0)
    else:
        print('Success to start!')

    print([line for line in stdout.readlines()])
    ssh.close()


if __name__ == '__main__':
    ssh_host = '192.168.1.2'
    ssh_user = 'user'
    ssh_pwd  = '123456'
    nginx_start(ipAddress='192.168.1.10', user='root', command='/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf', ssh_host, ssh_user, ssh_pwd, )
    nginx_stop(ipAddress='192.168.1.10', user='root')