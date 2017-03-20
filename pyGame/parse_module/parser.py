import jsonpickle

from pyhop_module import pyhop


#Import all user generated classes for pyhop functionaility

class parser():
    file_path = "C:\Users\Bnol\Desktop\pyhop_files"

    def dump_to_file(self,file_name):
        #Encode using json_pickle to preapre for file input
        jp_object = jsonpickle.encode(self)
        #Open new file or exisiting file for writing
        f = open(self.file_path+"\\"+file_name)
        #write to the file
        f.write(jp_object)
        f.close()

    def read_file(self,file_name):
        #Load File specififed by user
        f = open(self.file_path+"\\"+file_name)
        #Read encoded object from file
        jp_object= f.read()
        #close file
        f.close()
        #Decode file back to its original object
        object = jsonpickle.decode(jp_object)
        #return object
        return object




