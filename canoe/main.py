from config import PythonConfig
from watch import start_watch
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-c', '--config', default='', dest='config',
                  help='path to config file')
parser.add_option('-m', '--module', default='', dest='module',
                  help='module name')

def main():
    (options, args) = parser.parse_args()

    conf = None
    if options.module:
        conf = PythonConfig(options.module)
        print conf
    elif options.config:
        pass
        #conf = Config.from_file(options.config)

    if not conf:
        raise SystemExit()

    start_watch(conf.get_canoe())

if __name__ == '__main__':
    main()
