import sys
from jennie.tasklist import install_bootstrap
from jennie.bootstrap import add_navbar

__version__ = '0.0.1'
__author__ = 'ASK Jennie Developer <saurabh@ask-jennie.com>'

def execute():
    '''
    Shell Commands

    jennie install bootstrap
    :return:
    '''
    if len(sys.argv) == 3:
        if sys.argv[1] == "install" and sys.argv[2] == "bootstrap":
            install_bootstrap()

    elif len(sys.argv) == 4:
        if sys.argv[1] == "bootstrap" and sys.argv[2] == "add":
            add_navbar(sys.argv[3])

    else:
        command = ' '.join(sys.argv)
        print ("Invalid command: {}, check jennie command list".format(command))

if __name__ == '__main__':
    execute()