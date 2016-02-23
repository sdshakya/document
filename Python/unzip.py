import os

def get_unzip():
    unzip = raw_input("Enter file name: ")
    os.popen("tar -zxvf %s" % (unzip))
    print"\n Please have the unzipped file"
if __name__=="__main__":
   get_unzip()
