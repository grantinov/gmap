"""
The objective for sshClient is to connect to a target ssh server

 Project Name: gmap
 Developed by grant.stokley
 Date:    12/01/2017
 Time:    09:12


Example usage()s):

"""
import os
import paramiko
import subprocess


def _get_ssh_client(self):
    config = paramiko.SSHConfig()
    config.parse(open(os.path.expanduser('~/.ssh/config')))
    host = config.lookup(self.inputs.hostname)
    if 'proxycommand' in host:
        proxy = paramiko.ProxyCommand(
            subprocess.check_output(
                [os.environ['SHELL'], '-c', 'echo %s' % host['proxycommand']]
            ).strip()
        )
    else:
        proxy = None
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host['172.16.37.254'], username=host['grant.stokley'], sock=proxy)
    return client
