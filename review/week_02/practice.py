class person():
    def __init__(self, param_name):
        self.name = param_name

    def talk(self):
        print("안녕하세요.", self.name, "입니다.")


person_1 = person("유재석")
person_1.talk()
