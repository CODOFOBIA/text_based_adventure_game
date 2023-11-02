# class child:
#     def run(self):
#         print("child")

# class parent(child):
#     def run(self):
#         print("parent")

# class inherit(parent):
#     def show(self):
#         super(parent, self).run()  # This calls the run method from the Parent class
#         super(child, self).run()  # This calls the run method from the Child class

# i = inherit()
# i.show()

# d1 = {"1" : "one",
#       "2" : "two"}

# print(d1.get("1") == "one")

# class A:
#     def __init__(self, name):
#       self.name = name
 
# class B(A):
#     def __init__(self, roll, name):
#       self.roll = roll

#       A.__init__(self, name)
 
# object = B(23, "rahul")
# print(object.name)

# li = [2, 3, 4, 5, 6, 6, 7, 8]

# for i in li:
#   # print(i)
#   if 4 in li:
#     print("true")

dic = {"House" : "A dark house, walking very carefully each step makes a creak on the floor", 
      "forest": "A snowy forest, littered with dead leaves and branches"}

print(dic.keys("House"))