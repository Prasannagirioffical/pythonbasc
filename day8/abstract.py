from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self, app):
        pass

    def run(self, app):
        self.process(app)

class Mobile(Computer):
    def process(self, app):
        print(f"Mobile is running {app}")

class Laptop(Computer):
    def process(self, app):
        print(f"Laptop is running {app}")

samsung = Mobile()
samsung.run("pubg")

