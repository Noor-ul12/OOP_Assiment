class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"total created objects is: {cls.count}")    


counts = Counter()
counts1 = Counter()
counts3 = Counter()

Counter.show_count()