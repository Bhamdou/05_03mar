class SubsystemA:
    def operation1(self):
        print("SubsystemA operation1")

    def operation2(self):
        print("SubsystemA operation2")


class SubsystemB:
    def operation1(self):
        print("SubsystemB operation1")

    def operation2(self):
        print("SubsystemB operation2")


class SubsystemC:
    def operation1(self):
        print("SubsystemC operation1")

    def operation2(self):
        print("SubsystemC operation2")

    def operation3(self):
        print("SubsystemC operation3")


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()
        self._subsystem_c = SubsystemC()

    def operation1(self):
        self._subsystem_a.operation1()
        self._subsystem_b.operation1()
        self._subsystem_c.operation1()

    def operation2(self):
        self._subsystem_a.operation2()
        self._subsystem_b.operation2()
        self._subsystem_c.operation2()

    def operation3(self):
        self._subsystem_c.operation3()


if __name__ == "__main__":
    facade = Facade()
    facade.operation1()
    facade.operation2()
    facade.operation3()