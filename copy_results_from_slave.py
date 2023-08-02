import paramiko

windowsslave4 = paramiko.SSHClient()
windowsslave4.set_missing_host_key_policy(paramiko.AutoAddPolicy())
windowsslave4.connect(hostname='192.168.211.183', username='nande',
            password='22031997', port=22, timeout=3)

sftp_client = windowsslave4_client.open_sftp()
sftp_client.get('C:\\smartwatch\\popupresults\\', 'C:\\smartwatch\\popupresults\\')
sftp_client.close()

windowsslave3 = paramiko.SSHClient()
windowsslave3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
windowsslave3.connect(hostname='192.168.211.183', username='nande',
            password='22031997', port=22, timeout=3)

sftp_client = windowsslave3_client.open_sftp()
sftp_client.get('C:\\smartwatch\\popupresults\\', 'C:\\smartwatch\\popupresults\\')
sftp_client.close()