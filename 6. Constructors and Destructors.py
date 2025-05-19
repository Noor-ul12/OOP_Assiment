

class LOgger:
    def __init__(self):           # Constructor
        print("Logger object is created")


    def __del__(self):              # Destructors
        print("Logger object is destroyed")


log = LOgger()         # Logger object is created

del log                # Logger object is destroyed

