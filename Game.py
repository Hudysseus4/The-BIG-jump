#I have to define many variables

First_Steps = 0
Mom_knows_best = 0
JUSTRELAX = 0
VeryRudeAwakening = 0
WiseWORDS = 0
Loop = 0
while Loop == 0: #In case the player makes a typo, they will reset. This is very important for grade twos.
    Title = """                        
     _______ _            ____ _____ _____        _                       
     |__   __| |          |  _ \_   _/ ____|      | |                      
        | |  | |__   ___  | |_) || || |  __       | |_   _ _ __ ___  _ __  
        | |  | '_ \ / _ \ |  _ < | || | |_ |  _   | | | | | '_ ` _ \| '_ \ 
        | |  | | | |  __/ | |_) || || |__| | | |__| | |_| | | | | | | |_) |
        |_|  |_| |_|\___| |____/_____\_____|  \____/ \__,_|_| |_| |_| .__/ 
                                                                    | |    
                                A Jabari Story                      |_|                           
    """
    print (Title)
    start = input("                           Press any button to start\n")
    print("                            Welcome to The Big Jump.\n")
    mode = input("                           (1)Play     (2)Achievements\n")
    if mode == "1":
        if First_Steps == 0:
            Loop = 1
            Name = input("What is your name?") #This allows us to personalize to the game to the player
            input("Nice to meet you, " + Name + ", in order to help you learn how to play, this beginning sequence will teach you how the game works. Press any button to move on from text.\n") 
            input("3...2...1...GO!")
            while Loop == 1:
                print("'" + Name + "! You and Andy are going to the pool soon, your bathing suit is drying outside.' says your mom.\n" )
                C1 = input("(1)Go to bedroom (2)Leave house (3)Go outside\n")
                if C1 == "1":
                    print("'Did you listen to what I said!'\n")
                elif C1 == "2":
                    print("'Why are you leaving! You don't have your bathing suit.'\n")
                elif C1 == "3":
                    Loop = 2
                    while Loop == 2:
                        print("You grab your bathing suit but need somewhere to change\n")
                        C2 = input("(1)Change in bedroom (2)Change Here (3)Change in kitchen\n")
                        if C2 == "2":
                            print("This isn't a good spot to change\n")
                        elif C2 == "3":
                            print("I wouldn't change in the kitchen\n")
                        elif C2 == "1":
                            Loop = 3
                            if First_Steps == 0: 
                                print("First Steps\nYou got your first achievement! Try to get them all!")
                                First_Steps = 1
                                print("You put your bathing suit on and leave the house. \n")
                                #Now the player is going into the real game
                                input("Heads up! Any choice you make you won't be able to go back on.\n")
        
        Loop = 3
        while Loop == 3:
            print("Wait...were  you supposed to go to Andy's house or is he supposed to go to your house?")
            C3 = input("(1)Go to his house (2)Wait here  (3)Check with mom\n")
            if C3 == "1":
                Loop = 4
                print("You go to his house and knock. His mom answers the door and says 'Aren't you supposed to be at the pool?'\nOH NO! Now you remember, you were supposed to meet at the pool.\n")
                while Loop == 4:
                    print("You sprint to the pool, and see Andy there. 'Where were you " + Name + ", you were supposed to help me jump off the diving board! The pool is almost closed!'")
                    C4 = input("(1)You should've reminded me! (2)I'm sorry, but at least I'm here.")
                    if C4 == "1":                           
                        Loop = 5
                        while Loop == 5:
                            print("'I'm not the one that was late!'")
                            C5 = input("(1)YOU SHOULD HAVE! TOLD ME! (2)You're right, let's jump. (3)Sorry, I shouldn't have said that.")
                            if C5 == "1":
                                Loop = 6
                                while Loop == 6:
                                    print("Andy jumps back after the response, 'Okay, okay, it was my fault, I should've reminded you. Can you help me jump?'\nThen you say 'Then jump! NOW!\n'Ca-can you go before me?'\n'Fine!'\n")
                                    Loop = 12
                                    while Loop == 12:
                                        print("You climb the diving board but aren't strong enough to jump after sprinting to the pool. In the end, neither of you jump and your day is wasted.")
                                        Loop = 0
                            elif C5 == "2":
                                Loop = 7
                                while Loop == 7:
                                    print("He climbs the ladder. 'Woah, this is high.'\n 'I...I don't know about doing this,' he stutters, 'This is really scary.\n")
                                    C6 = input("(1)The Hardest Jump is your first    (2)It's easy!    (3)You can do it!")
                                    if C6 == "1" or C6 == "3":
                                        Loop = 8
                                        while Loop == 8:
                                            if WiseWORDS == 0: 
                                                print("\nWISE WORDS\n")
                                                WiseWORDS = 1
                                            print("What did you just say?")
                                            C7 = input("(1)You need to be brave   (2)What are you scared about?    (3)Jump!")
                                            if C7 == "1":
                                                Loop = 9
                                                while Loop == 9:
                                                    print("Okay then...Andy looks down to the water then back up.\n 'Let's do this!' he says, shaking a lot.\n")
                                                    C8 = input("(1)Breath in, then out    (2)Just go already    (3)Jump like Superman!")
                                                    if C8 == "1" or C8 == "3":
                                                        Loop = 10
                                                        while Loop == 10:                                                     
                                                            print("Andy breathes in...then out, then jumps, in an epic pose.")
                                                            Splash = """
                                                                       .---. ,---.  ,-.      .--.     .---. .-. .-. 
                                                                      ( .-._)| .-.\ | |     / /\ \   ( .-._)| | | | 
                                                                     (_) \   | |-' )| |    / /__\ \ (_) \   | `-' | 
                                                                        \ \  | |--' | |    |  __  | _  \ \  | .-. | 
                                                                    ( `-'  ) | |    | `--. | |  |)|( `-'  ) | | |)| 
                                                                     `----'  /(     |( __.'|_|  (_) `----'  /(  (_) 
                                                                            (__)    (_)                    (__)   
                                                                                """
                                                            print (Splash) #I love this wet font for the splash, the key moment in the story.
                                                            print("Andy climbs out the pool fast, is he hurt? Scared? Nope! He runs right to the diving board to jump again!")
                                                            print("Andy keeps doing jumps and once you recovered after the sprint, so do you.")
                                                            print("After a great jumping session at the pool, you and Andy go back to your houses. Whenever Andy is nervous, he thinks back to this time.")
                                                            if JUSTRELAX == 0: 
                                                                print("Just Relax and Splash")
                                                                JUSTRELAX = 1
                                                                Loop = 0
                                    elif C6 == "2":
                                        Loop = 11
                                        while Loop == 11:
                                            print("'Then why don't you do it?'")
                                            C9 = input("(1)I'm too tired to do it    (2)'Okay!'")
                                            if C9 == "1":                                              
                                                print("Breathe, in...then out. That's how I did it.")
                                                print("'In...out...in...out.'")
                                                Loop = 10
                                            elif C9 == "2":
                                                Loop = 12
                                                print("You climb up the diving board but you aren't strong enough to jump.")
                                                print("Neither of you jump, the day was wasted.")
                                                Loop = 0
                                            else: 
                                                print("Wrong input\n") 
                                    else:
                                        print("Wrong input\n")
                            else:
                                print("Wrong input\n")           
                    elif C4 == "2":
                        print("It's fine, let's go to the diving board and jump.")
                        C12 = input("(1)Oh yeah!     (2)Let's start with normal jumps.")
                        if 1 == "1":
                            print("You are tired after the run and tell him to go ahead.\nAndy walks over to the diving board and climbs up, smiling.\nAs he gets up to the top, he instantly starts shaking, as it it was freezing outside.\n'I...I don't know about this,' he stutters, 'This is really scary.'")
                            C6 = input("(1)The Hardest Jump is your first    (2)It's easy!    (3)You can do it!")
                            if C6 == "1" or C6 == "3":
                                Loop = 8
                                while Loop == 8:
                                    if WiseWORDS == 0: 
                                        print("\nWISE WORDS\n")
                                        WiseWORDS = 1
                                    print("What did you just say?")
                                    C7 = input("(1)You need to be brave   (2)What are you scared about?    (3)Jump!")
                                    if C7 == "1":
                                        Loop = 9
                                        while Loop == 9:
                                            print("Okay then...Andy looks down to the water then back up.\n 'Let's do this!' he says, shaking a lot.\n")
                                            C8 = input("(1)Breath in, then out    (2)Just go already    (3)Jump like Superman!")
                                            if C8 == "1" or C8 == "3":
                                                Loop = 10
                                                while Loop == 10:                                                     
                                                    print("Andy breathes in...then out, then jumps, in an epic pose.")
                                                    Splash = """
                                                                   .---. ,---.  ,-.      .--.     .---. .-. .-. 
                                                                  ( .-._)| .-.\ | |     / /\ \   ( .-._)| | | | 
                                                                 (_) \   | |-' )| |    / /__\ \ (_) \   | `-' | 
                                                                    \ \  | |--' | |    |  __  | _  \ \  | .-. | 
                                                                ( `-'  ) | |    | `--. | |  |)|( `-'  ) | | |)| 
                                                                 `----'  /(     |( __.'|_|  (_) `----'  /(  (_) 
                                                                        (__)    (_)                    (__)   
                                                                            """
                                                    print (Splash) #I love this wet font for the splash, the key moment in the story.
                                                    print("Andy climbs out the pool fast, is he hurt? Scared? Nope! He runs right to the diving board to jump again!")                                                       
                                                    print("Andy keeps doing jumps and once you recovered after the sprint, so do you.")
                                                    print("After a great jumping session at the pool, you and Andy go back to your houses. Whenever Andy is nervous, he thinks back to this time.")
                                                    if JUSTRELAX == 0: 
                                                        print("Just Relax and Splash")
                                                        JUSTRELAX = 1
                                                    Loop = 0
                                            elif C8 == "2":
                                                print("No! I won't jump I'm too scared. You're not helping.")
                                                print("GAME OVER")
                                                Loop = 0
                                            else: 
                                                print("Wrong input\n")
                                    elif C7 == "2" or C7 == "3":
                                        print("You're making this too hard! I won't jump.\n No one jumps, your day is wasted.\n GAME OVER")  
                                        Loop = 0          
                            elif C6 == "2":
                                Loop = 11
                                while Loop == 11:
                                    print("'Then why don't you do it?'")
                                    C9 = input("(1)I'm too tired to do it    (2)'Okay!'")
                                    if C9 == "1":                                              
                                        print("Breathe, in...then out. That's how I did it.")
                                        print("'In...out...in...out.'")
                                        Loop = 10
                                        while Loop == 10:                                                     
                                            print("Andy breathes in...then out, then jumps, in an epic pose.")
                                            Splash = """
                                                      .---. ,---.  ,-.      .--.     .---. .-. .-. 
                                                     ( .-._)| .-.\ | |     / /\ \   ( .-._)| | | | 
                                                    (_) \   | |-' )| |    / /__\ \ (_) \   | `-' | 
                                                       \ \  | |--' | |    |  __  | _  \ \  | .-. | 
                                                   ( `-'  ) | |    | `--. | |  |)|( `-'  ) | | |)| 
                                                    `----'  /(     |( __.'|_|  (_) `----'  /(  (_) 
                                                           (__)    (_)                    (__)  
                                                                """
                                            print (Splash) #I love this wet font for the splash, the key moment in the story.
                                            print("Andy climbs out the pool fast, is he hurt? Scared? Nope! He runs right to the diving board to jump again!")
                                            print("Andy keeps doing jumps and once you recovered after the sprint, so do you.")
                                            print("After a great jumping session at the pool, you and Andy go back to your houses. Whenever Andy is nervous, he thinks back to this time.")
                                            if JUSTRELAX == 0: 
                                                print("Just Relax and Splash")
                                                JUSTRELAX = 1
                                            Loop = 0
                                    elif C9 == "2":
                                        Loop = 12
                                        print("You climb up the diving board but you aren't strong enough to jump.")
                                        print("Neither of you jump, the day was wasted.")
                                        Loop = 0
                                    else: 
                                        print("Wrong input\n") 
                            else:
                                print("Wrong input\n")
                    else:
                        print("Wrong input")
            elif C3 == "2":
                print("You wait, then wait, and wait, guess what you do next? Wait.")
                print("GAME OVER-wait don't worry, each time you make a mistake you will learn what not to do.")
                Loop = 0
            elif C3 == "3":
                print("'Am I going to Andy's house or are is he going here?' 'Neither, you're meeting him at the pool.'\n")
                if Mom_knows_best == 0: 
                    print("Mom Knows Best\n")
                    Mom_knows_best = 1
                Loop = 13
                while Loop == 13:
                    print("You dash over to the pool and get there eventually. Andy arrives shortly after. There is quite a big line for the diving board.")
                    C10 = input("(1)Skip the line  (2)Wait in the line  (3)Do some warm-up jumps")
                    if C10 == "1":
                        Loop = 14
                        while Loop == 14: 
                            print("'Hey stop it! No breaking the rules! Get out of here' Says the lifeguard.")
                            print("GAME OVER")
                            Loop = 0
                    elif C10 == "2":
                        Loop = 15
                        while Loop == 15:
                            print("Andy's energy slowly goes down as you wait in line and he is acting like a zombie when it is finally his turn.")
                            print("'ohhh...it's my turn. just let me wake up'")
                            C11 = input("(1)Pull out the drums  (2)Let him wake up by himself  (3)Shake him")
                            if C11 == "1":
                                if VeryRudeAwakening == 0: 
                                    print("VERY RUDE AWAKENING")
                                    VeryRudeAwakening = 1
                                print("'I'm up now, and energized! He climbs up the the ladder quickly.'")
                                Splash = """
                                   .---. ,---.  ,-.      .--.     .---. .-. .-. 
                                  ( .-._)| .-.\ | |     / /\ \   ( .-._)| | | | 
                                 (_) \   | |-' )| |    / /__\ \ (_) \   | `-' | 
                                 _  \ \  | |--' | |    |  __  | _  \ \  | .-. | 
                                ( `-'  ) | |    | `--. | |  |)|( `-'  ) | | |)| 
                                 `----'  /(     |( __.'|_|  (_) `----'  /(  (_) 
                                        (__)    (_)                    (__)   
                                                                    """
                                print (Splash)
                                #I love this wet font for the key story moment.
                                print("Andy climbs out the pool fast, is he hurt? Scared? Nope! He runs right to the diving board to jump again!")
                                print("Andy keeps doing jumps and once you recovered after the sprint, so do you.")                                                                        
                                print("After a great jumping session at the pool, you and Andy go back to your houses. Whenever Andy is nervous, he thinks back to this time.")
                                if JUSTRELAX == 0: 
                                    print("Just Relax and Splash")
                                    JUSTRELAX = 1
                                Loop = 0
                    elif C10 == "3":
                        Loop = 10
                        while Loop == 10:
                            print("As you do warm up jumps, the line get massive...ly smaller. You get in the line when no one is left and Andy is ready to go") 
                            print("Okay then...Andy looks down to the water then back up.\n 'Let's do this!' he says, shaking a lot.\n")
                            C8 = input("(1)Breath in, then out    (2)Just go already    (3)Jump like Superman!")
                            if C8 == "1" or C8 == "3":
                                Loop = 16
                                while Loop == 16:                                                     
                                    print("Andy breathes in...then out, then jumps, in an epic pose.")
                                    Splash = """
                                            .---. ,---.  ,-.      .--.     .---. .-. .-. 
                                           ( .-._)| .-.\ | |     / /\ \   ( .-._)| | | | 
                                          (_) \   | |-' )| |    / /__\ \ (_) \   | `-' | 
                                             \ \  | |--' | |    |  __  | _  \ \  | .-. | 
                                         ( `-'  ) | |    | `--. | |  |)|( `-'  ) | | |)| 
                                          `----'  /(     |( __.'|_|  (_) `----'  /(  (_) 
                                                 (__)    (_)                    (__)   
                                                                                """
                                    print (Splash) #I love this wet font for the splash, the key moment in the story.
                                    print("Andy climbs out the pool fast, is he hurt? Scared? Nope! He runs right to the diving board to jump again!")
                                    print("Andy keeps doing jumps and once you recovered after the sprint, so do you.")
                                    print("After a great jumping session at the pool, you and Andy go back to your houses. Whenever Andy is nervous, he thinks back to this time.")
                                    if JUSTRELAX == 0: 
                                        print("Just Relax and Splash")
                                        JUSTRELAX = 1
                                    Loop = 0
                            elif C8 == "2":
                                print("No! I won't jump I'm too scared. You're not helping.")
                                print("GAME OVER")
                                Loop = 0
                            else:
                                print("Wrong input\n")
                    else: 
                        print("Wrong input\n")                                           
            else: 
                print("Wrong input\n")
    elif mode == "2":
        Loop = 20
        while Loop == 20:
            print("Achievements Collected:\n")        #This is a great way to get the player to replay the game and explore different options
            if First_Steps == 1:
                print("First Steps: You completed the tutorial.\n")
            if Mom_knows_best == 1:
                print("Mother Knows Best: You asked your mom for help.")
            if JUSTRELAX == 1:
                print("Just Relax: You helped Andy make a big splash.")
            if VeryRudeAwakening == 1:
                print("Very Rude Awakening: You woke Andy up rudely, very rudely.")
            if WiseWORDS == 1:
                print("Wise Words: You inspired Andy or confused him.")
            input("Press ANY button to return")
            Loop = 0
    else:
        print("Wrong input\n")
