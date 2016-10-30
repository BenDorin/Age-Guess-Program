import random
Benra = random.randint(12, 15)
print ("random age generated: " + str(Benra))
print ("How old is Ben? (*hint *hint he's between 12-15)")
Ben = input()
print ("Ben is " + Ben + " acording to you that is")
print ("Are you completely sure? (type 1 for yes and anything else for no)") 
YorN = input()

if YorN == "1":
    print (" Really you think Ben is " + Ben)
else:
    print ("Ok so you think Ben is how old?")
    Ben = input()
	
if Ben == str(Benra):
   print (" Wow !!!! you really are magical, Ben is indead "  + Ben)
else:
   print (" Ha... you're rubbish at this, his real age is " + str(Benra))
   print("you really thought Ben could be " + Ben)
   print("ahahah")
   
print ("Thanks For Playing")

