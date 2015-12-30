class adder:
    def __init__(self, value = 0):
        self.data = value

    def __add__(self, other):
        self.data += other

class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data

    def __repr__(self):
        return 'addboth(%s)' % self.data

if __name__='__main__':
    x = addboth(4)
    x+1
    x   # Runs __repr__
    print(x)    # Runs __str__