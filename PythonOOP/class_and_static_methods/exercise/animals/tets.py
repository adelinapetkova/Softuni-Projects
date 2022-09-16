from class_and_static_methods.exercise.animals.cat import Cat
from class_and_static_methods.exercise.animals.dog import Dog
from class_and_static_methods.exercise.animals.kitten import Kitten
from class_and_static_methods.exercise.animals.tomcat import Tomcat

dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
