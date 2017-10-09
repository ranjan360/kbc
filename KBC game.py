flag=True
questions_list = ["Which of these sounds would you associate with the heart ?","Who is the 'Bharat Ka Veer Putra Aaccording to the title of a 2013 TV Series?","In 2013, where did the natural calamity known as Himalayan tsunami occur?","Which film is this song from ?","In the Ramayana, Which demon impersonated Rama's voice, screaming, 'Lakshman! Help me'?","Who is the only leader to be elected Prime Minister of Pakistan three times ?","The black widow, which eats the male counterpart after mating, as a female species of which animal?","Douglas Engelbert, who passed away in 2013, is credited as the inventor of which of these products?","In 1850, the first experimental electric telegraph line in India was set up between Calcutta and which place?","Which of these persons has not walked on the Moon?","With Which of these states do Chhattisgarh, Jharkhand and Andhra Pradesh all share their borders?","The first world championship in what sport is planned to be held in 2017, though the game has been played since 1877?","Which is the largest living species of tortoise in the world, which may weigh about 400 kg?","According to legend, which of these Rishis regained his youth by a celestial favor ?","On a restaurant menu, which of these items is often listed as 'Jeera', 'Curd', 'Boiled' or 'Fried'?"]
# ek question list banaya hai usme aur 15 question dale hain.
option1_list = ["Tring Tring", "Tipu Sultan",         "Uttrakhand",        "Mere Dad Ki Maruti",  "Surpanakha",  "Syed Yousaf Raza Gillani",  "Sloth",   "Mobile Phone",    "Diamond Harbour",   "Charles Duke",      "Madhya Pradesh",      "Test Cricket",          "Sulcata Tortoise",       "Agastya",        "Manchurian"]
# ek option1_list banaya hain aur usme sare question ke pehle option dale hain.
option2_list = ["Tap Tap",     "Chandragupta Maurya", "Arunachal Pradesh", "Chennai Express",     "Khara",       "Benazir Bhutto",            "Ant",     "Computer Mouse",  "Darjeeling",        "James A Lovell",    "Odisha",              "Rugby Union",           "Grenada Tortoise",       "Durvasa",        "Burger"]
# ek option2_list banaya hain aur usme sare question ke doosre option dale hain.
option3_list = ["Click Click", "Maharana Pratap",     "Jammu and Kashmir", "Ghanchakkar",         "Maricha",     "Liaqat Ali Khan",           "Spider",  "Bluetooth Mouse", "Murshidabad",       "Alan Bean",         "Bihar",               "Kabaddi",               "Golden Greek Tortoise",  "Chyavana",       "Rice"]
# ek option3_list banaya hain aur usme sare question ke teesre option dale hain.
option4_list = ["Dhak Dhak",   "Ashoka",              "Sikkim",            "Race 2",              "Dushana",     "Nawaz Sharif",              "Termite", "Digital camera",  "Dhaka",             "Pete Conrad",       "Uttar Pradesh",       "Carrom",                "Galapagos Tortoise",     "Charaka",        "Pasta"]
# ek option4_list banaya hain aur usme sare question ke chautha option dale hain.
answer_list = (4,3,1,2,3,4,3,4,4,2,2,1,3,3,3)
# ab hamne answer list banaya hain aur usme sare question ke sahi answer dale hain.
prize  = (1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,"25lakh","50lakh","1cr")
# ab hamne ek prize list banai hain usme hamne 1000 se lekar 1cr tak ki prize dali hain.
padav = [0,0,0,0,10000,10000,10000,10000,10000,320000,320000,320000,320000,320000,"1cr"]
for index in range(15):
    if flag:
        print "apka question yeh hai"
        print "q-",questions_list[index]
        print "1-",option1_list[index]
        print "2-",option2_list[index]
        print "3-",option3_list[index]
        print "4-",option4_list[index]
        var1 = (raw_input("enter your answer\n"))
        if var1 == "quit":
            print "Aap ne game se quit kar liya hai. Par aaj aap ghar le kar ja rahe hai",padav[index], "rupees."
            flag = False
        elif int(var1) == answer_list[index]:
           print "congrats, sahi jawaab"
           print "aap",prize[index], "jeet chuke hai"
        else:
            var1!=answer_list[index]
            flag=False
            print "aapne galat ans diya hai aapka game khatam hua"
            print "ajj aap",padav[index],"jeet chuke ho."
        if prize[index]==10000:
            print "aapka pehla padav pura huaa"
        if prize[index]==320000:
            print "aapka dusra padav pura huaa"
        if prize[index]=="1cr":
            print "Congrats aap 1 crore jeet chuke ho"
