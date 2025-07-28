from .transport import Transport

class Sea(Transport):
    def __init__(self):
        print("[+] Sea Transportation invoked!")
    
    def run(self):
        print("[>>>] Running by Sea!")