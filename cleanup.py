import traceback
class cleaner():
    def __init__(self, holder, okAction = None, okArgs = (), badAction = None, badArgs = (), printer = print):
        self.holder = holder
        self.okAction = okAction
        self.okArgs = okArgs
        self.badAction = badAction
        self.badArgs = badArgs
        self.printer = printer
        self.stopped = False
        self.excTF = False
    def __enter__(self):
        pass
    def __exit__(self, *args):
        #Get the string equivalent of the exception
        excStrs = traceback.format_exception(*args)
        excPrintStr = '\n'
        for excStr in excStrs:
            excPrintStr += excStr
        #Check if exception actually occurred or if manager is just exiting
        if excPrintStr != '\nNoneType: None\n':
            self.excTF = True
        #Take action based on the situation
        if not self.stopped and self.excTF:
            self.printer("Exception in {}. Printing traceback:{}".format(self.holder, excPrintStr))
            if self.badAction != None:
                self.printer("Cleaning up after exception in {}.".format(self.holder))
                self.badAction(*self.badArgs)
            else:
                self.printer("No cleanup action specified for {}.".format(self.holder))
            self.stopped = True
        elif not self.stopped and not self.excTF:
            self.printer('Context manager in {} exiting. No exceptions occurred.'.format(self.holder))
            if self.okAction != None:
                self.okAction(*self.okArgs)
            else:
                self.printer('No clean exit action specified for {}.'.format(self.holder))
        else:
            self.printer("Cleanup has already occured.")