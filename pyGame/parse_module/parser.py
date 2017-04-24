import jsonpickle


class Parser:
    """This class is used to save and load user plans and any other user data
    that needs to be maintained between runs.

    The dump_to_file method may be used the write the contents of any python
    object to a JSON file.

    The read_file method may be used to read in and reconstruct any object
    that was saved to a JSON file using the dump_to_file method.
    """

    file_path = ""

    def dump_to_file(self, object, file_name):
        """Save an object to a JSON file of the provided name

        NOTE: The file path should be set before calling this method.
        NOTE 2: As of the current implementation (4/23/17) existing
        files are overwritten without warning.

        :param Object object: the object to be saved
        :param str file_name: the desired file name
        """
        jp_object = jsonpickle.encode(object)           # Encode using json_pickle to prepare for file writing
        f = open(self.file_path+"\\"+file_name, "w+")   # Open new file or existing file for writing
        f.write(jp_object)                              # Write to the file
        f.close()                                       # Close file

    def read_file(self,file_name):
        """Construct and return an object from a JSON file of the provided name

        NOTE: The file path should be set before calling this method.

        :param str file_name: JSON file from which the object is to be constructed
        :return: the object constructed from the JSON file of the provided name
        """
        f = open(self.file_path+"\\"+file_name)     # Load File specified by user
        jp_object = f.read()                        # Read encoded object from file
        f.close()                                   # Close file
        object = jsonpickle.decode(jp_object)       # Decode file back to its original object
        return object                               # Return the reconstructed object