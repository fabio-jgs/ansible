import winrm

s = winrm.Session('192.168.15.21', auth=('fabio', 'fabio'))
r = s.run_cmd('ipconfig', ['/all'])
r.status_code
r.std_out
r.std_err

