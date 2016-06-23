import os, sys

class ApiKeyManager():
    def __init__(self):
        self.mailgun_key = None
        self.librato_key = None

    def read_key(self, key_name):
        path = 'keys/' + key_name
        if os.path.exists(path):
            api_key = open(path, "r").read()
            if (len(api_key) != 0):
                return api_key
            else:
                return "{file_name} key file is empty. Exiting".format(file_name=path)
                sys.exit()
        else:
            print "{file_name} file not found. Exiting".format(file_name=path)
        sys.exit()

    def get_key(self, key_name):
        key_variable = 'self.{key_name}_key'.format(key_name=key_name)
        if key_variable in ['librato', 'mailgun'] and eval(key_variable):
            return eval(key_variable)
        else:
            return "{key_name} key is empty. Exiting".format(file_name=key_name)
            sys.exit()

    def set_key(self, librato_key, mailgun_key):
        self.librato_key = librato_key
        self.mailgun_key = mailgun_key
