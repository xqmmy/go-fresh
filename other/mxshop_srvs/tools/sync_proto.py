import os
import sys
import subprocess
import shutil


"""
    功能：
        1. 拷贝python的proto到go的对应目录之下
        2. 生成python的源码 - import .
        3. 生成go的源码
"""

class cd:
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def replace_file(file_name):
    new_file_name = f"{file_name}-bak"
    modify_times = 0   # 统计修改次数
    f1 = open(file_name,'r',encoding='utf-8')    # 以“r”(只读)模式打开旧文件
    f2 = open(new_file_name,'w',encoding='utf-8')  # 以“w”(写)模式打开或创建新文件（写模式下，文件存在则重写文件，文件不存在则创建文件）
    for lines in f1: # 循环读
        if lines.startswith("import") and not lines.startswith("import grpc"):
            lines = f"from . {lines}"
            modify_times += 1  # 每修改一次就自增一次
        f2.write(lines) # 将修改后的内容后的内容写入新文件
    print('文件修改的次数：',modify_times) # 9
    f1.close()  # 关闭文件f1
    f2.close()  # 关闭文件f2(同时打开多个文件时，先打开的先关闭，后打开的后关闭)
    os.replace(new_file_name,file_name) # 修改(替换)文件名


def proto_file_list(path):
    flist = []
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            proto_file_list(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for file in files:
        if file.endswith(".proto"):
            flist.append(file)
    return flist


def copy_from_py_to_go(src_dir, dst_dir):
    proto_files = proto_file_list(src_dir)
    for proto_file in proto_files:
        try:
            shutil.copy(f"{src_dir}/{proto_file}", dst_dir)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())


def generated_pyfile_list(path):
    flist = []
    lsdir = os.listdir(path)
    dirs = [i for i in lsdir if os.path.isdir(os.path.join(path, i))]
    if dirs:
        for i in dirs:
            proto_file_list(os.path.join(path, i))
    files = [i for i in lsdir if os.path.isfile(os.path.join(path, i))]
    for file in files:
        if file.endswith(".py"):
            flist.append(file)
    return flist


class ProtoGenerator:
    def __init__(self, python_dir, go_dir):
        self.python_dir = python_dir
        self.go_dir = go_dir

    def generate(self):
        with cd(self.python_dir):
            files = proto_file_list(self.python_dir)
            subprocess.call("workon mxshop_srv", shell=True)
            for file in files:
                command = f"python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. {file}"
                subprocess.call(command)

            #查询生成的py文件并添加上 from .
            py_files = generated_pyfile_list(self.python_dir)
            for file_name in py_files:
                replace_file(file_name)
            print(py_files)

        with cd(self.go_dir):
            files = proto_file_list(self.go_dir)
            for file in files:
                command = f"protoc -I . {file} --go_out=plugins=grpc:."
                subprocess.call(command)


class PyProtoGenerator:
    def __init__(self, python_dir):
        self.python_dir = python_dir

    def generate(self):
        with cd(self.python_dir):
            files = proto_file_list(self.python_dir)
            subprocess.call("workon mxshop_srv", shell=True)
            for file in files:
                command = f"python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. {file}"
                subprocess.call(command)

            #查询生成的py文件并添加上 from .
            py_files = generated_pyfile_list(self.python_dir)
            for file_name in py_files:
                replace_file(file_name)
            print(py_files)


if __name__ == "__main__":
    #goods的proto生成
    # python_dir = "C:\\Users\\Administrator\\PycharmProjects\\mxshop_srvs\\userop_srv\\proto"
    # go_dir = "D:\\python微服务\\projects\\mxshop-api\\userop-web\\proto"
    # #
    # # #将py目录下的文件夹拷贝到go目录下
    # copy_from_py_to_go(python_dir, go_dir)
    # #
    # # #生成对应的py源码和go源码
    # gen = ProtoGenerator(python_dir, go_dir)
    # gen.generate()

    py_gen = PyProtoGenerator("C:\\Users\\Administrator\\PycharmProjects\\mxshop_srvs\\inventory_srv\\proto")
    py_gen.generate()