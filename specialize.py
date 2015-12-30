class Super:
    def method(self):
        print('in Super.method')  # Default behavior

    def delegate(self):  # Expected to be defined
        self.action()

    def action(self):  # if this version is called
        assert False, "action must be defined"
        # or using raise NotImpelementedError('action must be defined')


class Inheritor(Super):  # Inherit method verbation
    pass


class Repalcer(Super):  # Replace method completely
    def method(self):
        print('in Replacer.method')


class Extender(Super):  # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')


class Provider(Super):  # Fill in a required method
    def action(self):
        print('in Provider.method')


if __name__ == '__main__':
    for klass in (Inheritor, Repalcer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
