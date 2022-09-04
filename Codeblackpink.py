import os
class Blackpink:
    job = "KPop idols"
    def __init__(self, name, age, role):
      self.name = name
      self.age = age
      self.role = role

jn = Blackpink('Kim Jennie', 26, 'Main rapper')
ls = Blackpink('Lalisa Manobal', 25, 'Main dancer')
js = Blackpink('Kim Jisoo', 27, 'Main visual')
rs = Blackpink('Park Chaeyoung', 25, 'Main vocal')
print('Jennie is one of the {}'.format(jn.__class__.job))
print("JN is 1 \nLS is 2 \nJS is 3 \nRS is 4")
stt = "" 
while stt=="":
    stt = input("Who do u want to learn about? ")
if int(stt) == 1:
    print("{} is {} years old, a {}".format( jn.name, jn.age, jn.role))
    os.startfile("C:\\Users\\ASUS\\Downloads\\solo.mp3")
elif int(stt) == 2:
    print("{} is {} years old, a {}".format( ls.name, ls.age, ls.role))
    os.startfile("C:\\Users\\ASUS\\Downloads\\lalisa.mp3")
elif int(stt) == 3:
    print("{} is {} years old, a {}".format( js.name, js.age, js.role))
    print("No solo yet:(")
elif int(stt) == 4:
    print("{} is {} years old, a {}".format( rs.name, rs.age, rs.role))
    os.startfile("C:\\Users\\ASUS\\Downloads\\ontheground.mp3")

