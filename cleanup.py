import traceback
class cleaner():
    def __init__(self, holder, action = None, args = (), printer = print):
        self.holder = holder
        self.action = action
        self.actionArgs = args
        self.printer = printer
        self.stopped = False
        return
    def __enter__(self):
        return
    def __exit__(self, *args):
        excStrs = traceback.format_exception(*args)
        excPrintStr = '\n'
        for excStr in excStrs:
            excPrintStr += excStr
        self.printer("Exception in {}. Printing traceback:{}".format(self.holder, excPrintStr))
        if not self.stopped:
            if self.action != None:
                self.printer("Cleaning up after exception in {}.".format(self.holder))
                self.action(*self.actionArgs)
            else:
                self.printer("No cleanup action specified for {}.".format(self.holder))
            self.stopped = True
        else:
            self.printer("Cleanup has already occured.")
        return