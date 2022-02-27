### MODULE: responsible for creating dynamic loggers and configuring a cli ###
import logging, os ,argparse, datetime

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d_%H-%M-%S")

class CLILogger:
    def __init__(self,log_name,loggers):
        self.args,self.parser = self._cli_config()
        if not self.args.command:
            self.log_lvl = logging.INFO
        else:
            self.log_lvl = self.args.log_level
        self.loggers = loggers
        self.log_name = log_name
        self._logging_config()
    def _logging_config(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        if not os.path.exists('logs'):
            os.mkdir('logs')
        if not os.path.exists(f'logs/{self.log_name}'):
            os.mkdir(f'logs/{self.log_name}')
        fh = logging.FileHandler(f'logs/{self.log_name}/{self.log_name}_{now}.log','w')
        fh.setLevel(self.log_lvl)
        formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
        fh.setFormatter(formatter)
        for log in self.loggers:
            logger = logging.getLogger(f'{log}')
            logger.addHandler(fh)
        infoLogger = logging.getLogger('console')
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        infoLogger.addHandler(sh)
    def _cli_config(self):
        def _add_options(parser):
            parser.add_argument('-v', '--verbose', help='add logging verbosity', action='store_const', dest='log_level', const=logging.DEBUG, default=logging.INFO)

        parser = argparse.ArgumentParser(description= f'micro automation service for Solicitor Credit Weekly Update Process')
        subparser = parser.add_subparsers(dest='command', metavar= '<command>', help='valid choices: {log} options: {-v}')

        explore_command = subparser.add_parser('log')
        explore_command.add_argument('log', help='log verbose', action= 'store_true')
        _add_options(explore_command)

        return parser.parse_args(), parser
