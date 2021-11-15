import argparse

def dimac_StartsWith_p(Input_Lines, name, info):
        Info = Input_Lines.pop(0)
        
        Input_Lines = [x[0:-1] for x in Input_Lines]
        
        if info:
                Number_of_Variables = Info[-2]
                Number_of_Clauses   = Info[-1]
                
                print(f"Number of Variables present in {name} : ", Number_of_Variables)
                print(f"Number of Clauses present   in {name}  : ", Number_of_Clauses)
                print(f"The first 5 clauses in {name} file :", Input_Lines[0:5])
                
                return Input_Lines 
        else:
                return Input_Lines    
    

def dimac_Reader(input_file, name, info = False): #DIMACS Reader; returns lists of lists
        Input_Lines = []
        for line in input_file.readlines():
                Input_Lines.append(line.strip("\n").split(" "))
        
        #Start of information extraction
        if Input_Lines[0][0] == 'c':
                Input_Lines =  Input_Lines[1:]
                dimac_StartsWith_p(Input_Lines, name, info)
            
        elif Input_Lines[0][0] == 'p':        
                dimac_StartsWith_p(Input_Lines, name,info)
        
        else:
                Input_Lines = [x[0:-1] for x in Input_Lines]  
                if info:
                        print(f"Number of Clauses present in {name} file  : ", len(Input_Lines))
                        print(f"The first 5 clauses in {name} file :", Input_Lines[0:5])
                        
                        return Input_Lines
                else:
                        return Input_Lines
            
        #End of information extraction
    

def play_Strategy(strategy_number, dimac_list): #Strategy Number, (Rules + Puzzle) -> input
        if strategy_number == 1:
                print("\nStrategy used is Davis–Putnam–Logemann–Loveland (DPLL) algorithm.")
                """
                    Code for DPLL
                """
    
        elif strategy_number == 2:
                print("\nStrategy used is Heuristic 2.")
                """
                   Code for Heuristic 2
                """        
    
        elif strategy_number == 3:
                print("\nStrategy used is Heuristic 3.")
                """
                   Code for Heuristic 3
                """          
    
def main():
    
    #___Rules + Game___#
        rules_file      = 'sudoku-rules.txt'
        game_file       = 'sudoku-example.txt'
        rules_plus_game = 'sudoku_nr_example.txt'
        
        filenames       = [rules_file, game_file] #[rules file name, example file name]
        with open(rules_plus_game,'w') as outfile:  #concatenation of Rules and Game
                for file in filenames:
                        with open(file) as infile:
                                outfile.write(infile.read())
                                
        #Getting the number of clauses in the game file to update the number of clauses in rules+game file
        lines_list    = open(rules_plus_game).readlines()
        
        if lines_list[0].split(" ")[0] == "c":
                temp          = lines_list[1].strip("\n").split()
        elif lines_list[0].split(" ")[0] == "p":
                temp          = lines_list[0].strip("\n").split()
        
        temp[-1]      = str(int(temp[-1]) + len(open(game_file).readlines())) + "\n"
        temp          = " ".join(temp)
        
        if lines_list[0].split(" ")[0] == "c":
                lines_list[1] = temp
        elif lines_list[0].split(" ")[0] == "p":
                lines_list[0] = temp
    
        open(rules_plus_game,'w').write("".join(lines_list))
    #__________________#
    
        parser = argparse.ArgumentParser()

        parser.add_argument("-S",   type = int, help = 'Pass strategy number 1 or 2 or 3 as arguments.')
        parser.add_argument("file", type = argparse.FileType('r'), help = 'Specify the name of the input file.')
    
        args                   = parser.parse_args()

        Strategy_Number, Input = args.S, args.file
    
    
        if Strategy_Number in [1,2,3]:
        
                Dimac_List = dimac_Reader(Input, args.file.name.strip('.txt').replace('-',' ').capitalize(), info = True) #Change info to True to obtain the number of clauses, variables and first 5 clauses
                play_Strategy(Strategy_Number, Dimac_List)
        
        else:
                print("Invalid Strategy Number\nChoose 1 or 2 or 3.")
    

if __name__ == "__main__":
        main()


      