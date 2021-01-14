import paramiko

def upload_file_to_server(local_path, remote_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    
    sftp = ssh.open_sftp()
    sftp.put(local, remote)
    return remote
