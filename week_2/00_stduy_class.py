class person:
    def __init__(self, param_name):
        print("i am created ", self)
        self.name = param_name

    def talk(self):
            print("안녕.", self.name)


person_1 = person("유재석")
print(person_1.name)
print(person_1)     # <__main__.person object at 0x0146E580>
person_1.talk()
