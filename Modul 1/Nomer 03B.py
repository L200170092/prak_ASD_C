#3b
def jmlhVokal(string):
    vkl = 0
    vokal = ["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]
    for i in string :
        if i in vokal :
            vkl+=1
            
    print(vkl)

jmlhVokal("Kartasura")
