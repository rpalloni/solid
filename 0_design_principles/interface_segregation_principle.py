# ISP: do not define too many methods in one class
# imposing useless implementation on class users

import numpy as np
from abc import ABC, abstractmethod

# one general-purpose interface
class Mammals(ABC):
    @abstractmethod
    def swim() -> bool:
        print("Can Swim")

    @abstractmethod
    def walk() -> bool:
        print("Can Walk")

class Human(Mammals):
    def swim():
        return print("Humans can swim")

    def walk():
        return print("Humans can walk")

class Whale(Mammals):
    def swim():
        return print("Whales can swim")


Human.swim()
Human.walk()

Whale.swim()
Whale.walk() # Can Walk: subclass whale can still invoke the method 'walk' but it should not!!!


# client-specific interfaces
class Walker(ABC):
  @abstractmethod
  def walk() -> bool:
    return print("Can Walk")

class Swimmer(ABC):
  @abstractmethod
  def swim() -> bool:
    return print("Can Swim")

class Human(Walker, Swimmer):
  def walk():
    return print("Humans can walk")
  def swim():
    return print("Humans can swim")

class Whale(Swimmer):
  def swim():
    return print("Whales can swim") # subclasses inherit only what is needed


##############################################################################


# all purpose machine: bad approach
class Machine:
    def prnt(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()


# ok if you need a multifunction device
class MultiFunctionPrinter(Machine):
    def prnt(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

# work around to skip not needed implementations
class OldFashionedPrinter(Machine):
    def prnt(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

### correct ISP approach
class Printer:
    @abstractmethod
    def prnt(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


# customize machine depending on needs
class MyPrinter(Printer):
    def prnt(self, document):
        print(document)

# multiinheritance: compose your machine
class Photocopier(Printer, Scanner):
    def prnt(self, document):
        print(document)

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def prnt(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def prnt(self, document):
        self.printer.prnt(document)

    def scan(self, document):
        self.scanner.scan(document)


printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
