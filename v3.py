import os
import subprocess
list_name = input("Please enter a site name.")
CDR_type = ['clr','oclr','com','ocom','data','odata','loan','mgr','omgr','mon','omon','rec','orec','MTrec','MTorec','sms','osms','vou','ovou']
CBP_Number_Tehran = ['101','102','103','104','105','106','107','108','109','110','111','145']
CBP_Number_Tabriz = ['123','124','125','126','127','128','129','130','131','132','133','146']
CBP_Number_Shiraz = ['112','113','114','115','116','117','118','119','120','121','122','147']
CBP_Number_Mashahd = ['134','135','136','137','138','139','140','141','142','143','144','148']
if list_name == 1:
    CBP_Number = CBP_Number_Tehran
elif list_name == 2:
    CBP_Number  = CBP_Number_Tabriz
elif list_name == 3:
    CBP_Number = CBP_Number_Shiraz
else:
    CBP_Number = CBP_Number_Mashahd
#date = os.system('date +"%Y-%m-%d"')
file_count = open('count.txt', 'w')

for type in CDR_type:
    for number in CBP_Number:
        file_name =type+"_"+number+'*.gz'
        cmd = 'zcat'+ ' ' + file_name +' ' '| wc -l'
        out = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr = subprocess.PIPE,stdin = subprocess.PIPE)
        stdout,stderr = out.communicate()
        print(stdout)
        file_count.write(file_name+": "+str(out) + '\n' )
file_count.close()