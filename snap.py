#snap is the name of the game 

def mk_str(str):
    if(str=="*"):
        return "a"
    elif(str=="**"):
        return "e"
    elif(str=="***"):
        return "i"
    elif(str=="****"):
        return "o"
    elif(str=="*****"):
        return "u"
    elif(str=="-1")or(str=="snap is the name of the game")or (str=="snap isn't the name of the game"):
        return ""
    else:
        return str[0]                

#driver code

prompt = input("What are we playing?: ")
answer = ""
answer2 = ""
collect=" "



while (prompt != '-1'):
    if(prompt=="snap is the name of the game")and(prompt!='-1'):
        while(prompt!="snap isn't the name of the game")and(prompt!='-1'):
            prompt=input("+")
            answer += mk_str(prompt)
    elif(prompt=="snap isn't the name of the game")and(prompt!='-1'):
        while(prompt!="snap is the name of the game")and(prompt!='-1'):
            prompt=input("+")
            answer2 += mk_str(prompt)
    else: 
        prompt= input("Wanna play snap?: ")



print("answer: ", answer, " ", answer2)









'''while (prompt != '-1'): 
    if (prompt == "snap is the name of the game"):
        while(collect!=('snap isn\'t the name of the game')): 
            answer+=(collect[0])
            collect = input("+")
            
    elif (prompt == "snap isn't the name of the game"):
        while(collect!=('snap is the name of the game')): 
            answer2+=(collect[0])
            collect = input("+")
    prompt = collect
print(answer, " ", answer2)'''
 


