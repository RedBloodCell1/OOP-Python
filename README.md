Today, i will start studying about Object Oriented Programming (OOP). I will try to FULLY UNDERSTAND all the concept within it.

Lets start:

## Day 1:

- Simple things, I learned something new which is what "self" inside a method. So the self itself is python by default pass 1 argument to the methods which is the class itself. wow...
- I will continue tomorrow. See you guys
- Oh a little update, you guys might wonder where have I been these days, well some days before, I just finished my thesis presentation and of course i still keep my promise of doing at least 1 meaningful problem each day. So yeah i did just that but i just didn't do it with my own laptop. So yeah, now im back here. thats cool

## Day 2:

- Lets continue. So `__init__` is called when we initiate an object
- **Instance attribute?** (OHHH so this means instance attribute is atribute that is assign on the function?)
- **Class attribute?** (So class attribute is simply attribute that is assign to the Class itself)
- What does attribute even mean? Is it like a variable with a value?
- So what i learned is, when a method doesnt find an attribute in its own method / instance, it will try to find it in the Class attribute
- So there is this magic attribute that i am going to list here for now on:
  - `__dict__` = To show the attribute inside a class or method
  - `__repr__` = Represent the address of the class variable / attribute

## Day 3:

### Class and Static Method

- Lets continue. I will finish this today
- **Class method?** What i know right now is, class method is something that doesnt automatically pass "self" inside of it but the "class object itself" is passed as the first argument
- **Static method?** So static method from what i know is just a function inside a class (method) that is not related to the class at all. It simply get its own parameter and is isolated alone and lonely like me. im kidding.

- **isinstance()** = passing 2 argument to check whether the 1st argument type is the 2nd argument
- **is_integer()** = Self explanatory (return boolean)

From my understanding:

- Use **Static Method** when something has a relationship with the class but it doesnt really need anything or do anything in the class itself. Its somekind of like a function outside the class, but we just put it inside because it has a relation with the class
- Use **Class Method** when something is related to the class and can change something within the class, like making a new item itself, or changing the class attribute itself.

### Inheritance

- **Inheritance** = This is the good part i am waiting at. This is the thing that i like. I can make games with this, characters, and everything. Damn its so simple but i never really understand this before. So inheritance is simply, we can make a new class that inherist all the attribute from the other class. Coolll

So the term Parent class & Child class is pretty self explanatory. Parent meaning its the parent, and the child inherit what its parent has.

- **`super().__init__(name, health, damage)`** = This is just super, like i mean its super cool. So to get mom's and dad's power, we need to call super method and initiate all the attribute like such. So then we can use all our parents power. Thats really cool. Theres a way to make it not dupe the `__init__` but he leave it for another time so its fine.

-`**class**.**name**= magic attribute to get the name of the class

### Getter and Setter

- Actually, i might not be able to keep my promise as I am pretty tired already... Damn, I don't expect this to brain fry me this much. Next is getter and setter. Lets go?

- **Encapsulation** = Idk, havent reach that yet. Probably like its name, only set one time and then no more

- **@property** = is a decorator like static and class method that is called before the function itself. This property decorator is so we can set something into read only (So you can't change it once its made)

- **Private Attribute** = Wow, this is something that i never wrap my head around before. This is simply an atribute that can only be accessed inside the class and not outside the class. damn its cool

- OHH so thats what getter and setter mean.

- **@name.setter** = We can set the name that we can't set anymore with this decorator. Thats cool. Its like a secret code within the class which can only be changed with another secret code from the class

- So getter, is when we try to get an attribute, and setter is when we try to set an attribute to a new name or anything. This is not confusing me because its pretty simple, but theres a lot of thing for my brain to consume. Well i believe in my brain so i will leave it to my brain to process all of this when i sleep.

- OHHH SO WE CAN ACTUALLY NOT SET UP THE NAME IN THE `__INIT__` BUT WE CAN USE SETTER TO MAKE SPECIAL CASE BEFORE SETTING A NAME... I don't really know how i can really apply this yet, or maybe i know, its just theres a lot of to consume today. so im once again fried

- I think I will continue this tomorrow. As I don't expect this to be this much. But I sure learn a lot today. See you tomorrow. Sorry for kinda breaking my promise. I will make it up for you guys today (Its already today). See youu

## Day 4:

- Im once again sorry that I am gone for a while, same reason, thesis, coping, lazy. But yeah, I am back here again. I will finish OOP today. Good news, my thesis is once again done. This time its done done like 95%. I can finally graduate. The thing is i still need to publish the paper. SO yeah i am waiting for that. But its done now.

- **Encapsulation** = So from what i learned, simply we can't access the attribute directly. but only allow it to access and modify it with a method inside the class

- **Abstraction** = OHHH. Its simply same as encapsulation, but instead of making an attribute private, we make a method private. We can do this by using "\_\_method" same as encapsulation

- **Inheritance** = I think i already know what this is? A child can inherit its parent method

- **Polymorphism** = Simply use of single type entity to represent multiple type of values. for example len() function in python can be used with integer, string, and list. So in OOP, we can have a method on the parent class that can handle multiple of its child. for example we can apply nerf of 0.8x to villain and nerf of 1x to npc. Well that is that. That all of OOP

I guess its not that hard, i just need to use it more and i will be proficient with it. Well, next im gonna do front end and back end thingies. So yeah see you for the next lesson.
