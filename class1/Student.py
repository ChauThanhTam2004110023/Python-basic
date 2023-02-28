class Student:
    count = 0
    def __init__(self,id,name):
        self._id = id
        self._name = name
        Student.count +=1

    @property
    def get_id(self):
        return self._id
    
    @get_id.setter
    def set_id(self,_id):
        self.id = _id

    def get_name(self):
        return self._name

    def set_name(self,_name):
        self.name = _name

    def show_info(self):
        print("Infomation Student")
        print(f"id: {self.id}, name: {self.name}")
        # print(f"name: {self.name}")