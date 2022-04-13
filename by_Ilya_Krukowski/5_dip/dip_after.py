import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message, printer):
        printer.write(f"{self.prefix} {message}")


logger = Logger()
printer = TerminalPrinter()
printer2 = FilePrinter()
logger.log("Starting the program...", printer)
logger.log("An error!", printer2)
