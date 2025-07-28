from .transport import Transport

class Air(Transport):
    def __init__(self):
        print("[+] Air Transportation invoked!")
    
    def run(self):
        print("[>>>] Running by Air!")