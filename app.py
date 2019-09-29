from flask import Flask
from flask import render_template
from flask import render_template_string
import os
app = Flask(__name__)


def get_folder_dic(root_folder):
    if not os.path.exists(root_folder):
        return {}
    ret_dic = {}
    ret_list = []
    for root,dirs,files in os.walk(root_folder,topdown=False):
        if dirs != []:
            break
        temp = []
        for file in files:
            temp.append(int(file.split('.')[0]))
        ret_dic[int(root.split('/')[-1])] = max([0] if temp == [] else temp)
        ret_list.append(int(root.split('/')[-1]))
    ret_list.sort()
    return ret_dic,ret_list

def get_filename(root_path):
    temp = []
    for i in os.listdir(root_path):
        temp.append(int(i.split('.')[0]))
    temp.sort()
    return temp

@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/index')
def index():
    col_num = 15
    row_num = 10
    preview_dic,preview_list = get_folder_dic('./static/preview_img')
    legends = [1,2,4,6,7,9,10,11,20]
    print(preview_list)
    return render_template('./index.html',preview_dic = preview_dic,preview_list=preview_list,\
                           col_num = col_num,row_num = row_num,legends = legends)

@app.route('/show/<string:work_id>')
def show(work_id):

    if not os.path.exists(os.path.join('./static/work/',work_id)):
        return render_template_string("No such work yet")
    file_list = get_filename(os.path.join('./static/work/',work_id))
    file_path = os.path.join('work/',work_id)
    
    return render_template('show.html',file_list = file_list,file_path = file_path)
    






if __name__ == '__main__':
    app.run()
