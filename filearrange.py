import shutil,os
try:
 os.chdir(input('Enter your path to arrange the files: '))
 files=list(filter(lambda x: os.path.splitext(x)[1],os.listdir()))
 ext=list(set(map(lambda y: os.path.splitext(y)[1].replace('.',''),files)))
 for i in ext:
  os.makedirs(i,exist_ok=True)
  for j in files:
   if i == os.path.splitext(j)[1].replace('.',''):
    shutil.move(j,i)
except Exception as e:print(f'an error occured: {e}')
    
    
   

