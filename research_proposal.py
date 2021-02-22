

print ("How old are you, pal?")
yearsOld = int(input())

print ("Hi, are you really", yearsOld, "years old?")

answer = str(input())
if answer == 'Yes' or 'yes' or 'yeah':
        print ("You didn't lie!")
elif answer == "yfdtfghjk":
        print ("You can't even give us a coherent answer!")
else: 
        print ("You live to lie, don't you?")
        

print ("Do you wish to take take part in my research?")

research = input()

research_list = ["maybe", 'maybe', "Maybe", "Maybe ", 'maybe ', "perhaps ", "perhaps", "Perhaps", "Perhaps ", "Idk", "idk", "idk ", "Idk "]
assert isinstance (research_list, list)

for item in research_list:
   if item == research:
	    match = item
	    print ("You got all the time in the world to think, my friend! Take care. ")
   else:
                    print ("Is that a yes that I've heard?!I hope to persuade you.")
                    yes_answer = input()
                    yes_answer_list = ["Yes", "yes", "ja", "yeah", "yeah!", "yeah " "yes ", "Yes ", "Yes..."]
                    assert isinstance (yes_answer_list, list)
                    for item in yes_answer_list:
                            if item == yes_answer:
                                    match = item
                                    print ("Thank you! I can't stop expressing my gratitide! Help...")

           
        

        
	         



 


