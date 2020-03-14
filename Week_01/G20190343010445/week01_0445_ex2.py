import socket
import sys
import time
import json

# http header attribute
HTTP__REQUEST_HEADERS = {'uri':'','Host':'', 
    'Connection':'', 
    'Cache-Control':'',
    'Upgrade-Insecure-Requests':'',
    'User-Agent':'',
    'Accept':'',
    'Accept-Encoding':'',
    'Accept-Language':''}

# parse http request header
def parse_http_request_header(request):
    request_content = request.splitlines()
    HTTP__REQUEST_HEADERS['uri'] = request_content[0]
    for r in request_content[1:-1]:
        if len(r)>0:
            tmp = r.split(':')
            # print('line 17:'+ str(tmp))
            HTTP__REQUEST_HEADERS[tmp[0]] = tmp[1]

# get request methond for example post,get. 
    method_type, uri = parse_http_request_method_uri(HTTP__REQUEST_HEADERS['uri'])

    # handle user's request with specified method
    if method_type in ('GET', 'HEAD'):
        return do_get_response(uri, HTTP__REQUEST_HEADERS['Accept'])
    elif method_type == 'POST':
        return do_post_response(uri, request_content[-1])
# parse uri 
def parse_http_request_method_uri(request_method):
    request_firstlines = request_method.split(' ')
    method_type = request_firstlines[0]
    uri = request_firstlines[1]
    print('uri is:'+method_type+' '+uri)
    return method_type, uri
# handle get method
def do_get_response(uri, content_type):
    print('do_get_response: ' + content_type)
    res = ''
    flag = 'rb'
    if content_type.find('text') != -1:
        flag = 'r'

    try:
        with open('.'+uri, flag) as f:
            # file = f.read(1024).encode('utf-8')
            if content_type.find('text/html') != -1:
                file = ''.join(f.readlines())
                # a = bytes(10)
                # a.
                return ('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n%s'%(len(file),file)).encode('utf8')
            
            if content_type.find('image') != -1:
                file = f.read(1024000)
                return bytes('HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: %d\r\n\r\n'%(len(file)), 'utf-8')+file
    except FileNotFoundError:
        print(uri+' not found!')
    http404 = 'HTTP/1.1 404 NOT FOUND %s \r\n\r\n'%(uri)
    return http404.encode('utf-8')

# handle post method
def do_post_response(uri, params):
    attrs = params.split('&')[:-1]
    print('do_post_response: '+ params+' '+ str(len(attrs)))
    attrs_dict = {attr.split('=')[0]:attr.split('=')[1]   for attr in attrs[:-2]}
    
    attrs = '<br>'.join(attrs)
    attrs = json.dumps(attrs)
    return bytes('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: %d\r\n\r\n%s'%(len(attrs),attrs),'utf-8')
    # return attrs_dict


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local host name
    hostname = socket.gethostname()
    local_ip = server_socket.getsockname()[0]

    port = 80
    print('server name:{0}'.format(hostname))
    # bind ip and port
    server_socket.bind((local_ip, port))


    # start to listen
    server_socket.listen(5)
    
    
    try:
        while True:
            msg = "welcome to gjwhttpserver!"
            print("wait for user's request!")
            time.sleep(1)
            server_socket.settimeout(5)
            client_socket, addr = server_socket.accept()
            print("connected from %s"% str(addr))
            recv = client_socket.recv(1024)
            request = recv.decode('utf-8')
            if len(request) == 0: 
                client_socket.sendall(bytes('','utf-8'))
                continue
            print(request)
            reponse_body = parse_http_request_header(request)
            client_socket.sendall(reponse_body)
            client_socket.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        server_socket.close()

