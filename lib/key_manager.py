import sys

class ApiKeyManager():
    def __init__(self):
        self.mailgun_key = None
        self.librato_key = None

    def get_key(self, key_name):
        key_variable = 'self.{key_name}_key'.format(key_name=key_name)
        if key_name in ['librato', 'mailgun'] and eval(key_variable):
            return eval(key_variable)
        else:
            return "{key_name} key is empty. Exiting".format(file_name=key_name)
            sys.exit()

    def set_keys(self, librato_key, mailgun_key):
        self.librato_key = librato_key
        self.mailgun_key = mailgun_key
