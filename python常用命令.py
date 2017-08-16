# 参数式命令行
import argparse
parser= argparse.ArgumentParser(description="""
说明：
 
""")
parser.add_argument('-i', help="输入文件名", default='')
parser.add_argument('-o', help="输出文件名", default='')
args= parser.parse_args()

imput=args.i
#输入文件   
ipn = raw_input("imput: ")


#############################R
library(showtext)
showtext.auto(enable = TRUE)
#font.add('SimSun', 'simsun.ttc')

#################################
adict={'superkingdom':'sk__','kingdom':'k__','phylum':'p__','class':'c__','order':'o__','family':'f__','genus':'g__','species':'s__'}


# list写入文件
import os,sys
path = os.getcwd()
list = os.listdir(path) #列出目录下的所有文件和目录

listfile = os.listdir(os.getcwd()) #目录下的所有文件
os.system('mkdir newdir') #运行系统命令
sys.argv[0]  #命令参数 

去除重复值
taaa=filter(lambda x : tax.count(x) == 1, tax)
  
列表list连接在一起  
taaa1=";".join(taaa)

def determine_group(groupfile):
    '''#判断groupfile文件是否存在'''
    import os
    if groupfile != '':
       if groupfile in os.listdir(os.getcwd()):
           return True
       else:
           print groupfile+'  Not Found********'
    else:
        return False
    

def unique(old_list):
    #得到unique列表
    newList = []
    for x in old_list:
        if x not in newList :
            newList.append(x)
    return newList  

namelist=[]
for i in os.listdir(os.getcwd()):
    if i.startswith(start) and i.endswith('.seq'):
        namelist.append(i)

#逐行读取文件
file = open("fa.txt","r")
keywoeds = ">"
for line in file:  
    if keywoeds in line:
     print >>outfile,line


#字典
dict_data = {}
with open(groups,'r') as df:
    for kv in [d.strip().split('\t') for d in df]:
     dict_data[kv[0]] = kv[1]

******************************************    
def readgroups(filename):
    '''#读取groups文件为字典'''
    dname={}
    dgroup={}
    with open(filename,'r') as df:
        for kv in [d.strip().split('\t') for d in df]:
            dname[kv[0]] = kv[1]
            dgroup.setdefault(kv[1],[]).append(kv[0])
    return {'dn':dname,'dg':dgroup}

	 
def read_dict(filename):
    '''读取文件为字典'''
    dict_data = {}
    with open(filename,'r') as df:
         for kv in [d.strip().split('\t') for d in df]:
             try:
                 dict_data[kv[0]] = kv[1]
             except:
                 print kv
    return dict_data
	
def readtable(filename):    
    '''读取table文件 .append or .extend '''  
    data = []
    for ln in open(filename,'rt'):
        data.append(ln.strip().split('\t'))
    return data

def readtable(filename):    
    #读取table文件 .append or .extend    
    data = []
    for ln in file(filename,'rt'):
        data2=[]
        for i in ln.strip().strip('\"').strip().split('\t'):
            data2.extend(i.strip('\"').split('\t'))
        data.append(data2)
    return data 

def write_data(flist,outname):
    #写入表格
    out=open(outname,'w')
    for i in flist:
        out.write('\t'.join(i)+'\n')
    out.close()
    
def readfa(faname):  #fasta文件名
    '''读取fasta'''
    data = []
    name = seq = ''
    for ln in file(faname,'rt'):
        if ln[0]=='>':
           data.append([name,seq])
           name=ln.strip()
           seq=''
        else:
           seq+=ln.strip()
    data.append([name,seq])
    return data[1:]

def reverse_seq(dna_list):
    '''dna_list='CATGCATCGT'
        序列反向互补
    '''
    RULE={'A':'T','T':'A','C':'G','G':'C'}
    return "".join(map(lambda x:RULE[x],dna_list))[::-1]


def readfq(fqname):  #fastq文件名
    '''#读取fastq'''
    data = []
    for ln in file(fqname,'rt'):
        data.append(ln.strip())
    data2=[]
    for i in range(int(len(data)/4)):
        data2.append(data[i*4:(i+1)*4])
    return data2


def write_faq(flist,outname):
    '''#写fq或fa'''
    out=open(outname,'w')
    for i in flist:
        out.write('\n'.join(i)+'\n')
    out.close()

def transpose(list2):
    '''转置'''
    data=[]
    for i in range(len(list2[0])):
        data1=[]
        for j in list2:
            data1.append(j[i])
        data.append(data1)
    return data          

#二维矩阵转置，list转置
tdata= map(list, zip(*data1))


#numpy模块的运用
a=numpy.array(list)
a.mean(),
a.std(),
a.std()/numpy.sqrt(len(a))])      

try：
     file("hello.txt", "r")                  #如果文件不存在，引发异常
     print "读文件"
except IOError:                              #捕获IO异常
     print "文件不存在"
except：                                     #其它异常
     print "程序异常" 
 
def torder(list1,n):
    #转置数组
    #list1=[[1, 4, 7, 'a', 'e'], [2, 19, 18, 'b', 'a'], [3, 6, 9, 'c', 'g']]
    list1=map(list, zip(*list1))
    list1.sort(key=lambda x:x[int(n)])
    return map(list, zip(*list1))

def pick_species(data,species):
     #选出species，放在第二行
     for i in data:
         if i[0]==species:
             data.remove(i)
             data.insert(1,i)
     return data

     
