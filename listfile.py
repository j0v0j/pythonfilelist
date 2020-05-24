import glob
class Filelist():
    def  __init__(self,filetype):
        self.filetype=filetype
    def listfile(self):#返回文件列表
        #recursive=True 不断进入文件夹遍历
        filelist = glob.glob(r"*/*."+self.filetype, recursive=False)
        return filelist

