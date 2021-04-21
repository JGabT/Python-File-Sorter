# put the program inside of the directory you want to sort then run it.
# https://github.com/JGabT/Python-File-Sorter (MIT-LICENSE)
import os 
import time
from pathlib import Path  

def ctdwn():
            print('will sort in 5 seconds. (ctrl-c to cancel now)')
            cdwn = 6
            while cdwn > 0:
                cdwn -= 1
                time.sleep(1)
                print(f"will proceed in {cdwn}")
            pass
def organize_junk(): 
   for entry in os.scandir(): 
       if entry.is_dir(): 
           continue
       file_path = Path(entry) 
       file_format = file_path.suffix.lower()
       if file_format and not str(file_path).startswith("pfs"): 
            ctdwn()
            directory_path = Path(file_format) 
            directory_path.mkdir(exist_ok=True) 
            file_path.rename(directory_path.joinpath(file_path)) 
            print(f'moved {file_path} to {directory_path}')

       for dir in os.scandir(): 
           try: 
               os.rmdir(dir) 
           except: 
               pass
 
if __name__ == "__main__": 
    organize_junk()