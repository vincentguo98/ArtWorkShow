import os

def get_folder_dic(root_folder):
    if not os.path.exists(root_folder):
        return {}
    ret_dic = {}
    for root,dirs,files in os.walk(root_folder,topdown=False):
        if dirs != []:
            break
        temp = []
        for file in files:
            temp.append(int(file.split('.')[0]))
        ret_dic[int(root.split('/')[-1])] = max([0] if temp == [] else temp)
    return ret_dic

def get_filename(root_path):
    temp = []
    for i in os.listdir(root_path):
        temp.append(int(i.split('.')[0]))
    temp.sort()
    return temp

if __name__ == '__main__':
    pass