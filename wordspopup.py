import nltk
import numpy as np
from test2 import convtoonesandzeros
from test import pointdist
import os
import colorama
from colorama import Fore
from nltk.corpus import wordnet


# Ensure that WordNet is downloaded
nltk.download('wordnet')

#starting the game by gathering a list of words using wordnet
#used a lot of chat gpt for word gathering(mega list and code using nltk)
def get_five_letter_words():
    five_letter_words = []
    win_condition = 0

    for synset in list(wordnet.all_synsets(pos='n')):
        for lemma in synset.lemmas():
            word = lemma.name()
            # Convert word to lowercase and check conditions
            #Wordnet tends to think things such as "20/20" is a 5 letter word, not in helps remove the fringe cases
            if len(word) == 5 and '_' not in word and '/' not in word and '1' not in word and '2' not in word and '-' not in word and word.lower() and "'" not in word not in five_letter_words:
                five_letter_words.append(word.lower())
                if len(five_letter_words) == 2500:
                    break
        if len(five_letter_words) == 2500:
            break






    #Using chat_gpt list to gather more words to add as well as editing the list
    five_letter_words = set(five_letter_words)
    five_letter_words = list(five_letter_words)
    five_letter_words.sort()
    five_letter_words.append("broke")
    five_letter_words.append("yours")
    five_letter_words.append("brawl")
    five_letter_words.remove("fagot")
    five_letter_words.append("idiot")
    five_letter_words.append("sixty")

    mega_words = [
        "about", "again", "apple", "avoid", "beach", "begun", "birds", "bloom", "bring", "built",
        "buyer", "candy", "cause", "chair", "charm", "chase", "cheer", "chess", "chief", "child",
        "claim", "clean", "clerk", "clock", "close", "cloud", "coach", "coast", "count", "cover",
        "crack", "cream", "crime", "dance", "death", "delay", "depth", "dream", "drink", "earth",
        "error", "event", "extra", "faith", "field", "final", "flame", "fleet", "floor", "force",
        "fresh", "fruit", "ghost", "glory", "grant", "grass", "great", "green", "greet", "group",
        "guard", "guest", "guide", "habit", "happy", "heart", "honey", "horse", "human", "humor",
        "ideal", "image", "inner", "issue", "juice", "laugh", "layer", "light", "limit", "lucky",
        "magic", "metal", "month", "music", "never", "night", "order", "outer", "peace", "power",
        "pride", "prove", "quick", "raise", "relax", "reply", "rough", "scene", "shape", "sleep",
        "books", "camps", "cards", "chairs", "chips", "clubs", "crabs", "dates", "doors", "drums",
        "ducks", "facts", "farms", "fears", "feats", "films", "fists", "flaws", "foods", "foots",
        "gifts", "goats", "grabs", "grins", "grows", "gulls", "hands", "hairs", "hills", "ideas",
        "items", "jokes", "lamps", "limbs", "lines", "lions", "loans", "lumps", "lures", "masks",
        "minds", "nests", "norms", "oaths", "pages", "parks", "pasts", "peaks", "pests", "plans",
        "plays", "plots", "pools", "posts", "prays", "preys", "rains", "rates", "rides", "rings",
        "risks", "roads", "rocks", "roles", "rooms", "roots", "rules", "saves", "sands", "seals",
        "seeds", "ships", "shots", "signs", "skies", "slabs", "slams", "slips", "slots", "snaps",
        "snows", "songs", "souls", "spots", "spurs", "stabs", "stems", "steps", "stirs", "stops",
        "swans", "tales", "tasks", "teams", "tests", "texts", "tiles", "times", "tones", "tools",
        "tours", "traps", "trees", "trips", "tubes", "turns", "vases", "verbs", "vices", "views",
        "vines", "walls", "waves", "weeks", "wines", "words", "yarns", "zones", "boats", "cakes",
        "clans", "clays", "clues", "coats", "coins", "crews", "cults", "cures", "deals", "discs",
        "dives", "downs", "edges", "files", "fires", "gates", "gears", "glows", "goals", "goods",
        "grips", "herbs", "hints", "hives", "hoops", "hopes", "icons", "jumps", "lakes", "leads",
        "leaps", "likes", "lists", "marks", "mints", "molds", "nodes", "pains", "paths", "peels",
        "pills", "pints", "pipes", "plows", "rails", "rants", "rides", "roots", "ruins", "sales",
        "scans", "seams", "shops", "sizes", "skins", "slaps", "songs", "stars", "stems", "stirs",
        "swaps", "tasks", "tides", "tools", "towns", "trays", "tubes", "votes", "wants", "waves",
        "wears", "weeds", "wings", "years"
    ]



    #Since list is from chat gpt, needs an extra check to make sure the word is really 5 letters long
    for i in range(len(mega_words)):
        if len(list(mega_words[i])) == 5:
            five_letter_words.append(mega_words[i])



    #switching from set to list helps remove repeats in list
    five_letter_words = set(five_letter_words)
    five_letter_words = list(five_letter_words)
    five_letter_words.sort()



    #lets player easily play again
    play_again = 1
    while play_again == 1:
        #this code will check weather or not the word typed is a vaild 5 letter words by checking weather or not the word typed
        #is part of the list of all five letter words that this program can generate
        good_word = 1
        while good_word == 1:
            guess1 = input("Type a 5 letter word....")
            u = []
            for i in range(len(five_letter_words)):
                if str(guess1.lower()) == five_letter_words[i]:
                    u.append(1)
            if sum(u) == 1:
                good_word = 2
            else:
                print("this word is not a valid response, please try again")
                input()
                good_word = 1




        # choosing which word out of the 500 to guess for
        which_word = np.random.randint(len(five_letter_words))
        ans_word = five_letter_words[which_word]


        #We need to find out if the word that the program picked out matches well with the word that was choosen by the player
        #Convert the 1st letter of the fisrt guess
        First_guess_point_total = []

        #These terms will be used for Keyboard Display later on, needs to be set up outside of the next loop
        alpha = ["q", 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
                 'c', 'v',
                 'b', 'n', 'm']
        ww = Fore.RESET
        bb = Fore.CYAN
        yy = Fore.YELLOW
        gg = Fore.GREEN
        alpha_color = [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww,
                       ww]
        #setting up varibles for futrure use
        color_on_guess = [ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww, ww,
                       ww,ww,ww,ww,ww]



        #This will tell us how many points we will get
        for j in range(len(guess1)):

            u1 = convtoonesandzeros(guess1,ans_word,ans_word[j])
            v1 = convtoonesandzeros(ans_word,ans_word,ans_word[j])

            #Now we use our function to compare the two words
            w1 = pointdist(u1,v1)

            #we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
            #how many points to award to the guesser
            First_guess_point_total.append(w1)





        given_points_for_first_guess = []
        for i in range(len(guess1)):
            given_points_for_first_guess.append(max(First_guess_point_total[0][i],First_guess_point_total[1][i],First_guess_point_total[2][i],First_guess_point_total[3][i],First_guess_point_total[4][i]))

        #assigning colors for the keyboard
        for i in range(len(given_points_for_first_guess)):
            for j in range(len(alpha)):
                if given_points_for_first_guess[i] == 0 and guess1[i] == alpha[j]:
                    alpha_color[j] = bb



        #Now we update the colors of the letters of our guess1
        #just for reminders, we defined the colors below
        #yy = Fore.YELLOW
        #gg = Fore.GREEN
        for i in range(len(given_points_for_first_guess)):
            if given_points_for_first_guess[i] == 1:
                color_on_guess[i] = yy
            if given_points_for_first_guess[i] == 2:
                color_on_guess[i] = gg

        #this is to test if we have won already, will be used to skip certain if statements if so
        if sum(given_points_for_first_guess) == 10:
            win_condition =1

        #dummy varible, does not do anything other than lets me avoid using not equal on certain for loops
        passon = 125


        #shows the score you got on the previous word



        if win_condition == 1:
            passon = 10
        else:
            print("You Have 5 More Guesses to Find the Word Out")
            input()
            good_word = 1
            while good_word == 1:
                clear = lambda : os.system('cls')
                clear()
                print(f"{alpha_color[0]}Q {alpha_color[1]}W {alpha_color[2]}E {alpha_color[3]}R {alpha_color[4]}T {alpha_color[5]}Y {alpha_color[6]}U {alpha_color[7]}I {alpha_color[8]}O {alpha_color[9]}P ")
                print(f"  {alpha_color[10]}A {alpha_color[11]}S {alpha_color[12]}D {alpha_color[13]}F {alpha_color[14]}G {alpha_color[15]}H {alpha_color[16]}J {alpha_color[17]}K {alpha_color[18]}L")
                print(f"  {alpha_color[19]}Z {alpha_color[20]}X {alpha_color[21]}C {alpha_color[22]}V {alpha_color[23]}B {alpha_color[24]}N {alpha_color[25]}M {ww}")
                print("")
                print("")
                print(f"        {color_on_guess[0]}{guess1[0].upper()}{color_on_guess[1]}{guess1[1].upper()}{color_on_guess[2]}{guess1[2].upper()}{color_on_guess[3]}{guess1[3].upper()}{color_on_guess[4]}{guess1[4].upper()}")




                #Now we re-run the word check for the second word typed
                guess2 = input("Guess...")
                u = []
                for i in range(len(five_letter_words)):
                    if str(guess2.lower()) == five_letter_words[i]:
                        u.append(1)
                if sum(u) == 1:
                    good_word = 2
                else:
                    print("this word is not a valid response, please try again")
                    input()
                    good_word = 1



                #We need a new list to tally the 2nd points total score
            second_guess_total_points = []



            #this is similar to what was here before
            for j in range(len(guess1)):
                u1 = convtoonesandzeros(guess2, ans_word, ans_word[j])
                v1 = convtoonesandzeros(ans_word, ans_word, ans_word[j])

                # Now we use our function to compare the two words
                w1 = pointdist(u1, v1)

                # we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
                # how many points to award to the guesser
                second_guess_total_points.append(w1)


            given_points_for_second_guess = []
            for i in range(len(guess1)):
                given_points_for_second_guess.append(
                    max(second_guess_total_points[0][i], second_guess_total_points[1][i], second_guess_total_points[2][i],
                        second_guess_total_points[3][i], second_guess_total_points[4][i]))

            # assigning colors for the keyboard
            for i in range(len(given_points_for_first_guess)):
                for j in range(len(alpha)):
                    if given_points_for_second_guess[i] == 0 and guess2[i] == alpha[j]:
                        alpha_color[j] = bb

            # Now we update the colors of the letters of our guess1
            # just for reminders, we defined the colors below
            # yy = Fore.YELLOW
            # gg = Fore.GREEN
            for i in range(len(given_points_for_first_guess)):
                if given_points_for_second_guess[i] == 1:
                    color_on_guess[i+5] = yy
                if given_points_for_second_guess[i] == 2:
                    color_on_guess[i+5] = gg

                # this is to test if we have won already, will be used to skip certain if statements if so
            if sum(given_points_for_second_guess) == 10:
                win_condition = 1





        #Now we do the loop for the 3rd Guess
        if win_condition == 1:
            passon = 10

        else:
            print("You Have 4 More Guesses to Find the Word Out")
            input()
            good_word = 1
            while good_word == 1:
                clear = lambda: os.system('cls')
                clear()
                print(
                    f"{alpha_color[0]}Q {alpha_color[1]}W {alpha_color[2]}E {alpha_color[3]}R {alpha_color[4]}T {alpha_color[5]}Y {alpha_color[6]}U {alpha_color[7]}I {alpha_color[8]}O {alpha_color[9]}P ")
                print(
                    f"  {alpha_color[10]}A {alpha_color[11]}S {alpha_color[12]}D {alpha_color[13]}F {alpha_color[14]}G {alpha_color[15]}H {alpha_color[16]}J {alpha_color[17]}K {alpha_color[18]}L")
                print(
                    f"  {alpha_color[19]}Z {alpha_color[20]}X {alpha_color[21]}C {alpha_color[22]}V {alpha_color[23]}B {alpha_color[24]}N {alpha_color[25]}M {ww}")
                print("")
                print("")
                print(
                    f"        {color_on_guess[0]}{guess1[0].upper()}{color_on_guess[1]}{guess1[1].upper()}{color_on_guess[2]}{guess1[2].upper()}{color_on_guess[3]}{guess1[3].upper()}{color_on_guess[4]}{guess1[4].upper()}")
                print(
                    f"        {color_on_guess[5]}{guess2[0].upper()}{color_on_guess[6]}{guess2[1].upper()}{color_on_guess[7]}{guess2[2].upper()}{color_on_guess[8]}{guess2[3].upper()}{color_on_guess[9]}{guess2[4].upper()}")








                # Now we re-run the word check for the second word typed
                guess3 = input("Guess...")
                u = []
                for i in range(len(five_letter_words)):
                    if str(guess3.lower()) == five_letter_words[i]:
                        u.append(1)
                if sum(u) == 1:
                    good_word = 2
                else:
                    print("this word is not a valid response, please try again")
                    input()
                    good_word = 1

                # We need a new list to tally the 2nd points total score
            third_guess_total_points = []

            # this is similar to what was here before
            for j in range(len(guess1)):
                u1 = convtoonesandzeros(guess3, ans_word, ans_word[j])
                v1 = convtoonesandzeros(ans_word, ans_word, ans_word[j])

                # Now we use our function to compare the two words
                w1 = pointdist(u1, v1)

                # we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
                # how many points to award to the guesser
                third_guess_total_points.append(w1)

            given_points_for_third_guess = []
            for i in range(len(guess1)):
                given_points_for_third_guess.append(
                    max(third_guess_total_points[0][i], third_guess_total_points[1][i], third_guess_total_points[2][i],
                        third_guess_total_points[3][i], third_guess_total_points[4][i]))

            # assigning colors for the keyboard
            for i in range(len(given_points_for_first_guess)):
                for j in range(len(alpha)):
                    if given_points_for_third_guess[i] == 0 and guess3[i] == alpha[j]:
                        alpha_color[j] = bb

            # Now we update the colors of the letters of our guess1
            # just for reminders, we defined the colors below
            # yy = Fore.YELLOW
            # gg = Fore.GREEN
            for i in range(len(given_points_for_first_guess)):
                if given_points_for_third_guess[i] == 1:
                    color_on_guess[i + 10] = yy
                if given_points_for_third_guess[i] == 2:
                    color_on_guess[i + 10] = gg

                # this is to test if we have won already, will be used to skip certain if statements if so
            if sum(given_points_for_third_guess) == 10:
                win_condition = 1



        # Now we do the loop for the 4th Guess
        if win_condition == 1:
            passon = 10

        else:
            print("You Have 3 More Guesses to Find the Word Out")
            input()
            good_word = 1
            while good_word == 1:
                clear = lambda: os.system('cls')
                clear()
                print(
                    f"{alpha_color[0]}Q {alpha_color[1]}W {alpha_color[2]}E {alpha_color[3]}R {alpha_color[4]}T {alpha_color[5]}Y {alpha_color[6]}U {alpha_color[7]}I {alpha_color[8]}O {alpha_color[9]}P ")
                print(
                    f"  {alpha_color[10]}A {alpha_color[11]}S {alpha_color[12]}D {alpha_color[13]}F {alpha_color[14]}G {alpha_color[15]}H {alpha_color[16]}J {alpha_color[17]}K {alpha_color[18]}L")
                print(
                    f"  {alpha_color[19]}Z {alpha_color[20]}X {alpha_color[21]}C {alpha_color[22]}V {alpha_color[23]}B {alpha_color[24]}N {alpha_color[25]}M {ww}")
                print("")
                print("")
                print(
                    f"        {color_on_guess[0]}{guess1[0].upper()}{color_on_guess[1]}{guess1[1].upper()}{color_on_guess[2]}{guess1[2].upper()}{color_on_guess[3]}{guess1[3].upper()}{color_on_guess[4]}{guess1[4].upper()}")
                print(
                    f"        {color_on_guess[5]}{guess2[0].upper()}{color_on_guess[6]}{guess2[1].upper()}{color_on_guess[7]}{guess2[2].upper()}{color_on_guess[8]}{guess2[3].upper()}{color_on_guess[9]}{guess2[4].upper()}")
                print(
                    f"        {color_on_guess[10]}{guess3[0].upper()}{color_on_guess[11]}{guess3[1].upper()}{color_on_guess[12]}{guess3[2].upper()}{color_on_guess[13]}{guess3[3].upper()}{color_on_guess[14]}{guess3[4].upper()}")

                guess4 = input("Guess...")
                u = []
                for i in range(len(five_letter_words)):
                    if str(guess4.lower()) == five_letter_words[i]:
                        u.append(1)
                if sum(u) == 1:
                    good_word = 2
                else:
                    print("this word is not a valid response, please try again")
                    input()
                    good_word = 1

                # We need a new list to tally the 2nd points total score
            fourth_guess_total_points = []

            # this is similar to what was here before
            for j in range(len(guess1)):
                u1 = convtoonesandzeros(guess4, ans_word, ans_word[j])
                v1 = convtoonesandzeros(ans_word, ans_word, ans_word[j])

                # Now we use our function to compare the two words
                w1 = pointdist(u1, v1)

                # we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
                # how many points to award to the guesser
                fourth_guess_total_points.append(w1)

            given_points_for_fourth_guess = []
            for i in range(len(guess1)):
                given_points_for_fourth_guess.append(
                    max(fourth_guess_total_points[0][i], fourth_guess_total_points[1][i],
                        fourth_guess_total_points[2][i],
                        fourth_guess_total_points[3][i], fourth_guess_total_points[4][i]))

            # assigning colors for the keyboard
            for i in range(len(given_points_for_first_guess)):
                for j in range(len(alpha)):
                    if given_points_for_fourth_guess[i] == 0 and guess4[i] == alpha[j]:
                        alpha_color[j] = bb

            # Now we update the colors of the letters of our guess1
            # just for reminders, we defined the colors below
            # yy = Fore.YELLOW
            # gg = Fore.GREEN
            for i in range(len(given_points_for_first_guess)):
                if given_points_for_fourth_guess[i] == 1:
                    color_on_guess[i + 15] = yy
                if given_points_for_fourth_guess[i] == 2:
                    color_on_guess[i + 15] = gg

                # this is to test if we have won already, will be used to skip certain if statements if so
            if sum(given_points_for_fourth_guess) == 10:
                win_condition = 1

        # Now we do the loop for the 5th Guess
        if win_condition == 1:
            passon = 10

        else:
            print("You Have 2 More Guesses to Find the Word Out")
            input()
            good_word = 1
            while good_word == 1:
                clear = lambda: os.system('cls')
                clear()
                print(
                    f"{alpha_color[0]}Q {alpha_color[1]}W {alpha_color[2]}E {alpha_color[3]}R {alpha_color[4]}T {alpha_color[5]}Y {alpha_color[6]}U {alpha_color[7]}I {alpha_color[8]}O {alpha_color[9]}P ")
                print(
                    f"  {alpha_color[10]}A {alpha_color[11]}S {alpha_color[12]}D {alpha_color[13]}F {alpha_color[14]}G {alpha_color[15]}H {alpha_color[16]}J {alpha_color[17]}K {alpha_color[18]}L")
                print(
                    f"  {alpha_color[19]}Z {alpha_color[20]}X {alpha_color[21]}C {alpha_color[22]}V {alpha_color[23]}B {alpha_color[24]}N {alpha_color[25]}M {ww}")
                print("")
                print("")
                print(
                    f"        {color_on_guess[0]}{guess1[0].upper()}{color_on_guess[1]}{guess1[1].upper()}{color_on_guess[2]}{guess1[2].upper()}{color_on_guess[3]}{guess1[3].upper()}{color_on_guess[4]}{guess1[4].upper()}")
                print(
                    f"        {color_on_guess[5]}{guess2[0].upper()}{color_on_guess[6]}{guess2[1].upper()}{color_on_guess[7]}{guess2[2].upper()}{color_on_guess[8]}{guess2[3].upper()}{color_on_guess[9]}{guess2[4].upper()}")
                print(
                    f"        {color_on_guess[10]}{guess3[0].upper()}{color_on_guess[11]}{guess3[1].upper()}{color_on_guess[12]}{guess3[2].upper()}{color_on_guess[13]}{guess3[3].upper()}{color_on_guess[14]}{guess3[4].upper()}")
                print(
                    f"        {color_on_guess[15]}{guess4[0].upper()}{color_on_guess[16]}{guess4[1].upper()}{color_on_guess[17]}{guess4[2].upper()}{color_on_guess[18]}{guess4[3].upper()}{color_on_guess[19]}{guess4[4].upper()}")


                guess5 = input("Guess...")
                u = []
                for i in range(len(five_letter_words)):
                    if str(guess5.lower()) == five_letter_words[i]:
                        u.append(1)
                if sum(u) == 1:
                    good_word = 2
                else:
                    print("this word is not a valid response, please try again")
                    input()
                    good_word = 1

                # We need a new list to tally the 2nd points total score
            fifth_guess_total_points = []

            # this is similar to what was here before
            for j in range(len(guess1)):
                u1 = convtoonesandzeros(guess5, ans_word, ans_word[j])
                v1 = convtoonesandzeros(ans_word, ans_word, ans_word[j])

                # Now we use our function to compare the two words
                w1 = pointdist(u1, v1)

                # we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
                # how many points to award to the guesser
                fifth_guess_total_points.append(w1)

            given_points_for_fifth_guess = []
            for i in range(len(guess1)):
                given_points_for_fifth_guess.append(
                    max(fifth_guess_total_points[0][i], fifth_guess_total_points[1][i],
                        fifth_guess_total_points[2][i],
                        fifth_guess_total_points[3][i], fifth_guess_total_points[4][i]))

            # assigning colors for the keyboard
            for i in range(len(given_points_for_first_guess)):
                for j in range(len(alpha)):
                    if given_points_for_fifth_guess[i] == 0 and guess5[i] == alpha[j]:
                        alpha_color[j] = bb

            # Now we update the colors of the letters of our guess1
            # just for reminders, we defined the colors below
            # yy = Fore.YELLOW
            # gg = Fore.GREEN
            for i in range(len(given_points_for_first_guess)):
                if given_points_for_fifth_guess[i] == 1:
                    color_on_guess[i + 20] = yy
                if given_points_for_fifth_guess[i] == 2:
                    color_on_guess[i + 20] = gg

                # this is to test if we have won already, will be used to skip certain if statements if so
            if sum(given_points_for_fifth_guess) == 10:
                win_condition = 1

                # Final Guess
        if win_condition == 1:
            passon = 10

        else:
            print("You Have 1 More Guesses to Find the Word Out, Good Luck")
            input()
            good_word = 1
            while good_word == 1:
                clear = lambda: os.system('cls')
                clear()
                print(
                    f"{alpha_color[0]}Q {alpha_color[1]}W {alpha_color[2]}E {alpha_color[3]}R {alpha_color[4]}T {alpha_color[5]}Y {alpha_color[6]}U {alpha_color[7]}I {alpha_color[8]}O {alpha_color[9]}P ")
                print(
                    f"  {alpha_color[10]}A {alpha_color[11]}S {alpha_color[12]}D {alpha_color[13]}F {alpha_color[14]}G {alpha_color[15]}H {alpha_color[16]}J {alpha_color[17]}K {alpha_color[18]}L")
                print(
                    f"  {alpha_color[19]}Z {alpha_color[20]}X {alpha_color[21]}C {alpha_color[22]}V {alpha_color[23]}B {alpha_color[24]}N {alpha_color[25]}M {ww}")
                print("")
                print("")
                print(
                    f"        {color_on_guess[0]}{guess1[0].upper()}{color_on_guess[1]}{guess1[1].upper()}{color_on_guess[2]}{guess1[2].upper()}{color_on_guess[3]}{guess1[3].upper()}{color_on_guess[4]}{guess1[4].upper()}")
                print(
                    f"        {color_on_guess[5]}{guess2[0].upper()}{color_on_guess[6]}{guess2[1].upper()}{color_on_guess[7]}{guess2[2].upper()}{color_on_guess[8]}{guess2[3].upper()}{color_on_guess[9]}{guess2[4].upper()}")
                print(
                    f"        {color_on_guess[10]}{guess3[0].upper()}{color_on_guess[11]}{guess3[1].upper()}{color_on_guess[12]}{guess3[2].upper()}{color_on_guess[13]}{guess3[3].upper()}{color_on_guess[14]}{guess3[4].upper()}")
                print(
                    f"        {color_on_guess[15]}{guess4[0].upper()}{color_on_guess[16]}{guess4[1].upper()}{color_on_guess[17]}{guess4[2].upper()}{color_on_guess[18]}{guess4[3].upper()}{color_on_guess[19]}{guess4[4].upper()}")
                print(
                    f"        {color_on_guess[20]}{guess5[0].upper()}{color_on_guess[21]}{guess5[1].upper()}{color_on_guess[22]}{guess5[2].upper()}{color_on_guess[23]}{guess5[3].upper()}{color_on_guess[24]}{guess5[4].upper()}")



                guess6 = input("Guess...")
                u = []
                for i in range(len(five_letter_words)):
                    if str(guess5.lower()) == five_letter_words[i]:
                        u.append(1)
                if sum(u) == 1:
                    good_word = 2
                else:
                    print("this word is not a valid response, please try again")
                    input()
                    good_word = 1

                # We need a new list to tally the 2nd points total score
            sixth_guess_total_points = []

            # this is similar to what was here before
            for j in range(len(guess1)):
                u1 = convtoonesandzeros(guess6, ans_word, ans_word[j])
                v1 = convtoonesandzeros(ans_word, ans_word, ans_word[j])

                # Now we use our function to compare the two words
                w1 = pointdist(u1, v1)

                # we need to append the w to First Guess Point Total so we can do opperatoins on all 5 of the letters to see
                # how many points to award to the guesser
                sixth_guess_total_points.append(w1)

            given_points_for_sixth_guess = []
            for i in range(len(guess1)):
                given_points_for_sixth_guess.append(
                    max(sixth_guess_total_points[0][i], sixth_guess_total_points[1][i],
                        sixth_guess_total_points[2][i],
                        sixth_guess_total_points[3][i], sixth_guess_total_points[4][i]))

            # assigning colors for the keyboard
            for i in range(len(given_points_for_first_guess)):
                for j in range(len(alpha)):
                    if given_points_for_sixth_guess[i] == 0 and guess6[i] == alpha[j]:
                        alpha_color[j] = bb

            # Now we update the colors of the letters of our guess1
            # just for reminders, we defined the colors below
            # yy = Fore.YELLOW
            # gg = Fore.GREEN
            for i in range(len(given_points_for_first_guess)):
                if given_points_for_sixth_guess[i] == 1:
                    color_on_guess[i + 25] = yy
                if given_points_for_sixth_guess[i] == 2:
                    color_on_guess[i + 25] = gg

                # this is to test if we have won already, will be used to skip certain if statements if so
            if sum(given_points_for_sixth_guess) == 10:
                win_condition = 1



        #checks win condition to see if player answer the right word
        clear = lambda: os.system('cls')
        clear()
        if win_condition == 1:
            print("Congrats You Win")
            print(f"The word was...{ans_word}")
        if win_condition != 1:
            print("Looks like you did not win")
            print(f"The answer word was...{ans_word}")

        input()

        #ask player if they want to play again
        print("press the x on the top corner if you want to stop playing")
        pg = input()
        if pg != 1:
            play_again = 1
            win_condition = 17





    return five_letter_words






get_five_letter_words()


