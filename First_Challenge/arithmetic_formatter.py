
def arithmetic_arranger(problems: list , showSolved: bool = False) -> str:
    #check for constrain len <= 5
    nro_problems = len(problems)
    if(nro_problems > 5):
        return "Error: Too many problems."
    
    
    #check Constrains
    problems_lst = []
    for problem in problems:
        temp_list = problem.split()
        
        for i in range(len(temp_list)):
            
            if(i % 2 == 0): #look for positons 0 and 2
                
                #check for constrain "Each number should only contain digits"
                try:
                    int(temp_list[i])
                except:
                    return "Error: Numbers must only contain digits."
                
                #check for constrain "Each number should only contain 4 digits"
                if(len(temp_list[i]) > 4):
                    return "Error: Numbers cannot be more than four digits."
                
            else:
                #check for constrain "just addition and subtraction"
                if not (temp_list[i] == "+" or temp_list[i] == "-"):
                    return "Error: Operator must be '+' or '-'."
        if(temp_list[1] == "+"):
            temp_list.append("a")
        else:
            temp_list.append("s")
    
        
        #after checking for constrains, operands and operator are added 
        problems_lst.append(temp_list)
    
    #graphin 
    upperNumbers = ""
    belowNumbers = ""
    hyphens = ""
    solutions = ""
    
    for problem in problems_lst:
        may_len = 0
        operand_1 = problem[0]
        operator = problem[1]
        operand_2 = problem[2]
        
        num_extraSpace = len(operand_1) - len(operand_2)
        
        upperNumbers += " " * 2
        if(num_extraSpace < 0):
            upperNumbers += " " * abs(num_extraSpace)
            may_len = len(operand_2)
            
        upperNumbers += operand_1 + " " * 4
        
        belowNumbers += operator + " "
        if(num_extraSpace > 0):
            belowNumbers += " " * abs(num_extraSpace)
            may_len = len(operand_1)
        elif(num_extraSpace == 0):
            may_len = len(operand_1)
        
        belowNumbers +=  operand_2 + " " * 4
        
        if(problem[3] == "a"):
            operationResult = int(operand_1) + int(operand_2)
        else:
            operationResult = int(operand_1) - int(operand_2)
        
        nrohyphens = 2 + may_len
        hyphens += "-" * nrohyphens + " " * 4
        
        solutions += (" " * (nrohyphens - len(str(operationResult)))) + str(operationResult) + " " * 4
        
    
    upperNumbers = upperNumbers.rstrip()
    belowNumbers =  belowNumbers.rstrip()
    hyphens = hyphens.rstrip()
    solutions = solutions.rstrip()
    
    arithmeticGraphic = upperNumbers + "\n" +   belowNumbers + "\n" + hyphens 
    if(showSolved):
        arithmeticGraphic += "\n" + solutions
    
    
    return arithmeticGraphic 

