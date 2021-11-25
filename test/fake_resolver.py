
class FakeResolver:

    def __init__(self):
        self.entries = {}

    def add(self, package, content):
        key = package + '.presentable_exceptions.presentable_exceptions'
        self.entries[key] = content
    
    def __call__(self, package):
        if package not in self.entries.keys():
            return None
        return self.entries[package]
