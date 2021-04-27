##########################################################################################
# Author : Eunjung Lee
# Date : 2020.02.25
# Purpose : Check the database and tag it.
# Usage : python filtering_tag.py input_file.vcf database1.vcf database2.vcf database3.vcf
# Python version : Python 3
##########################################################################################

file1 = "/home/ez/Research/PNET/WGS/germline/LSC-13N.haplotyper.filtered.final.vcf"
dbsnp = "/home/ez/Reference/dbsnp/dbsnp_138.b37.vcf"
gnomad = "/home/ez/Reference/gnomad/gnomad.exomes.r2.1.1.sites.AF_eas_kor.0.01-2.vcf"
krg = "/home/ez/Reference/KRG/KRG1722.vcf"

###############################################################


## dbsnp
dbsnp_dic = {}
with open(dbsnp) as ifp:
    for x in ifp:
        if x[0] != '#':
            x_1 = x.strip().split('\t')
            key = '%s_%s_%s_%s' % (x_1[0], x_1[1], x_1[3], x_1[4])
            if key in dbsnp_dic:
                pass
            else:
                dbsnp_dic[key] = x_1[6]

## gnomad
gnomad_dic = {}
with open(gnomad) as ifp:
    for x in ifp:
        if x[0] != '#':
            x_1 = x.strip().split('\t')
            key = '%s_%s_%s_%s' % (x_1[0], x_1[1], x_1[3], x_1[4])
            if key in gnomad_dic:
                pass
            else:
                gnomad_dic[key] = x_1[6]

## KRG
krg_dic = {}
with open(krg) as ifp:
    for x in ifp:
        if x[0] != '#':
            x_1 = x.strip().split('\t')
            key = '%s_%s_%s_%s' % (x_1[0], x_1[1], x_1[3], x_1[4])
            if key in krg_dic:
                pass
            else:
                krg_dic[key] = x_1[6]


## germline match
germline_dic = {}
new_file = ""
a = 0
with open(file1) as ifp:
    for x in ifp:
        if x[0] != '#':
            x_1 = x.strip().split('\t')
            key = '%s_%s_%s_%s' % (x_1[0], x_1[1], x_1[3], x_1[4])
            if key in germline_dic:
                pass
            else:
                germline_dic[key] = x_1[6]
            if key in dbsnp_dic:
                x_1[6] = 'dbsnp=YES'
            else:
                x_1[6] = 'dbsnp=NO'
            if key in gnomad_dic:
                x_1[6] = x_1[6] + ',gnomad=YES'
            else:
                x_1[6] = x_1[6] + ',gnomad=NO'
            if key in krg_dic:
                x_1[6] = x_1[6] + ',krg=YES'
            else:
                x_1[6] = x_1[6] + ',krg=NO'
            new_x_1 = '\t'.join(x_1)
            new_file += new_x_1+"\n"
            print('The working chromosome is number %s.' % x_1[0])


fw = open("tagged", 'w')
fw.write(new_file)
fw.close()
print("tagged", "is SAVED!")


quit()