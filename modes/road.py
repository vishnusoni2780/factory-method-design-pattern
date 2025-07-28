from .transport import Transport

class Road(Transport):
    def __init__(self):
        print("[+] Road Transportation invoked!")
    
    def run(self):
        print("[>>>] Running by Road!")