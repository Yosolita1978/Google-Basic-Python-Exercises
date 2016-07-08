""" This program will help you decide is you should eat chocolate. Hint: you should """

def eat_chocolate():
    print "Eat it, eat some chocolate"

def what_happened():
    options = ("""
    What Happened?:  
        1. Didn't get funding
        2. Experiment didn't work
        3. Lab is on fire
        4. Bureaucracy

        """)
    answer = raw_input(options)
    return answer

def main():
    while True:
        prompt1 = "How's your Day"\
        + "\n" + "1 - Good" + "\n" + "2 - Bad" + "\n"
        choice = int(raw_input(prompt1))
        if choice == 1:
            print "Well done, have a reward"
            eat_chocolate()
        elif choice == 2:
            question = what_happened()
            if question == "1":
                print "Sucks!, You'll need energy to write a new grant application"
                eat_chocolate()
            elif question == "2":
                print "Better walk to the shops to think up a new one"
                eat_chocolate()
            elif question == "3":
                print "You might be in shock, you should keep your blood sugar up"
                eat_chocolate()
            elif question == "4":
                print "Chocolate requires no paper work"
                eat_chocolate()
            else:
                break

if __name__ == '__main__':
    main()