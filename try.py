
# Discrete Structures: Section A



def print_list(list):
    ret = ""
    for i in range(len(list)):
        ret += list[i]

    return (ret)


def inverse(equation):
    list = []
    stop = len(equation)    
    for i in range(len(equation)):
        list.append(equation[i])

    # print (list)

    if '~' not in list:
        list.insert(0,'~')
        list.insert(4,'~')
        print(print_list(list), "this is the inverse of the equation: ", equation)

    elif list[0] and list[4] =='~':
        while '~' in list:
            list.remove('~')
        print(print_list(list), "this is the inverse of the equation: ", equation)


    elif list[0] == '~':
        list.remove('~')
        list.insert(3,'~')
        print(print_list(list), "this is the inverse of the equation: ", equation)

    elif list[3] == '~':
        list.remove('~')
        list.insert(0,'~')
        print(print_list(list), "this is the inverse of the equation: ", equation)

    # print (list)



def converse(equation):

    list = []
    stop = len(equation)    
    for i in range(len(equation)):
        list.append(equation[i])

    # print (list)

    if '~' not in list:
        var = list[0]
        list[0] = list[3]
        list[3] = var
        print(print_list(list), "this is the converse of the equation: ", equation)

    elif list[0] and list[4] == '~':
        var = list[1]
        list[1] = list[5]
        list[5] = var
        print(print_list(list), "this is the converse of the equation: ", equation)


    elif list[3] == '~':
        var = list[4]
        var1 = list[0]
        list[0] = var
        list[4] = var1

        list.remove('~')
        list.insert(0, '~')
        print(print_list(list), "this is the converse of the equation: ", equation)


    elif list[0] == '~':
        list.remove('~')
        var = list[0]
        list[0] = list[3]
        list[3] = var
        list.insert(3, '~')
        print(print_list(list), "this is the converse of the equation: ", equation)



    # print (list)

def contrapositive(equation):
    list = []
    stop = len(equation)    
    for i in range(len(equation)):
        list.append(equation[i])


    if '~' not in list:
        list.insert(0,'~')
        list.insert(4,'~')

        var = list[1]
        list[1] = list[5]
        list[5] = var
        print(print_list(list), "this is the contrapositive of the equation: ", equation)

    elif list[0] and list[4] == '~':
        while '~' in list:
            list.remove('~')
        var = list[0]
        list[0] = list[3]
        list[3] = var
        print(print_list(list), "this is the contrapositive of the equation: ", equation)

    elif list[3] =='~':
        list.remove('~')
        # list.insert(3,'~')
        var = list[0]
        list[0] = list[3]
        list[3] = var
        list.insert(3,'~')
        print(print_list(list), "this is the contrapositive of the equation: ", equation)

    elif list[0] == '~':
        list.remove('~')

        var = list[0]
        list[0] = list[3]
        list[3] = var
        list.insert(0,'~')

        print(print_list(list), "this is the contrapositive of the equation: ", equation)



def implication(equation):

    list = []
    stop = len(equation)    
    for i in range(len(equation)):
        list.append(equation[i])

    
    if "-" and ">" not in list:
        raise Exception("This is not an Implication!")
    else:
        print("The equation: " + equation + " is an implication")

    

def propositional_logic(equation, type):
    
    implication(equation)
    inverse(equation)
    contrapositive(equation)
    converse(equation)


propositional_logic("~p->q", "implication")
# propositional_logic("~p->q", "implication")
# propositional_logic("~p->q", "implication")
# propositional_logic("~p->q", "implication")
    
            
    

    

    
        

    