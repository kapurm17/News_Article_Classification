import os
import pandas as pd

PATH=os.getcwd()

def get_folders(path):
    '''
    Get the list of folders in the specified path
    Args:
        path: provide path to the directory, else checks the current directory by default

    Returns:
        list of folders in the specified path
    '''
    lst =os.listdir(path)
    folders = [f for f in lst if os.path.isdir(os.path.join(path,f)) == True]
    return folders

#print(get_folders())

def read_files(folder, path):
    '''
    reads the files' content and saves it in a list
    Args:
        path: base path of the directory with different class folders
        folder: teh folder with the files

    Returns:
        lis of read documents
    '''
    path_files = os.path.join(path, folder)
    files = os.listdir(path_files)
    #print(len(files))
    lst=[]
    for f in files:
        try:
            with open(os.path.join(path_files, f), 'r') as new:
                lst.append(new.read().encode('utf-8').strip())
        except:
            pass
    #print(lst[0])
    return lst

#print(read_files(folder=get_folders()[4]))


def main(path=PATH):
    '''
    Coverts a directory based classes' text data to an excel sheet
    Args:
        Base path to the folder which contains class wise directories

    Returns:
        An excel sheet named data.xlsx
    '''
    print('Do you want to specify a path other than the main directory? Y/N')
    if input() == 'Y':
        print('Enter Path \n')
        path = input()
    else:
        pass

    folders= get_folders(path)
    print(folders)
    target = []
    text = []
    for f in folders:
        print(f)
        tmp = []
        tmp_f = read_files(f, path) 
        text.extend(tmp_f)
        tmp.append(f)
        target.extend(tmp * len(tmp_f))
        print(len(target), len(tmp_f))
        print('DONE')
    df=pd.DataFrame({'target': target, 'text': text})
    df.to_excel('data.xlsx')

    return None

main()

