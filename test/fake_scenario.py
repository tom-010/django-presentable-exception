from presentable_exception.presentable_exception import ExceptionScenario

class FakeScenarioLoader:

    def __init__(self):
        self.lut = {}
        self.default_package = 'package'

    def register(self, key, package=None, description=None, responsible='server'):
        self.register_scenario(ExceptionScenario(
            package=package or self.default_package, 
            key=key, 
            description=description or key, 
            responsible=responsible))

    def register_scenario(self, scenario):
        self.lut[scenario.package + '.' + scenario.key] = scenario

    def to_scenario(self, package, key):
        return self.lut.get(package + '.' + key)

class FakeScenario:

    def __init__(self, package, key,  message, log_entry, responsible='server'):
        self.package = package
        self.key = key
        self.message = lambda data: message
        self.log_entry = lambda data: log_entry
        self.responsible = responsible