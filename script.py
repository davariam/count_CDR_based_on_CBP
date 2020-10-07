import os
CDR_type = ['clr','oclr','com','ocom','data','odata','loan','mgr','omgr','mon','omon','rec','orec','MTrec','MTorec','sms','osms','vou','ovou']
CBP_Number = ['101','102','103','104','105','106','107','108','109','110','111','145','123','124','125','126','127','128','129','130','131','132','133','146','112','113','114','115','116','117','118','119','120','121','122','147','134','135','136','137','138','139','140','141','142','143','144','148']
print(len(CBP_Number))
print(len(CDR_type))
print(len(CDR_type)*len(CBP_Number))
for type in CDR_type:
    for number in CBP_Number:
        file_name =type+"_"+number+'*.gz'
        cmd = 'zcat'+ ' ' + file_name +' ' '| wc -l'
        #print(cmd)


        #print(file_name)

