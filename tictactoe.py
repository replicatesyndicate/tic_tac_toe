def tictactoe():
    #importing
    from IPython.display import clear_output
    import time
    #initializing
    replay = "Y"
    board_clear = ["_", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    board_example = ["_", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = {"X":"","O":""}
    #valid_move = False
    goal = "play"
    board_index = 0    
    #################################################################################
    
    #FUNCTIONS
    
    #Turn function: Executes player turns, and applies valid moves.        
    def user_turn(order):
        valid = False
        while valid == False:
            
            #Print the player turns
            board_input = int(input("Your turn, Player {}. Please enter cell number.".format(player[order])))
                        
            #check if move is valid, and request another input if invalid move.
            if board_input in range(1,10):
                valid = board[board_input] == " "
                if valid == False: 
                    print("Invalid move.")
            else:
                print("Please enter a number in range 1-9")
                
        #if valid move, return move. switch players for next turn.
        return board_input
        
    
    #Display function - displays board
    def display_board():
        clear_output()
        print(board[7]+"|"+board[8]+"|"+board[9])
        print("-|-|-")
        print(board[4]+"|"+board[5]+"|"+board[6])
        print("-|-|-")
        print(board[1]+"|"+board[2]+"|"+board[3])
    
    #Goal checker function - checks if game is over
    def goal_check(turns):
        for i in range(1,10):
            #Win conditions

            #diagonal
            if board[1]==board[5]==board[9] or board[7]==board[5]==board[3]:
                if board[5] != " ":
                    return board[5]

            elif i<4:
                #horizontal-bottom row
                if i%3==0: 
                    if board[i]==board[i-1]==board[i-2]:
                        if board[i] != " ":
                            return board[i]
                #vertical
                elif board[i]==board[i+3]==board[i+6]:
                    if board[i] != " ":
                        return board[i]

            elif board[3]==board[6]==board[9]:
                if board[6] != " ":
                    return board[6]
            elif board[4]==board[5]==board[6]:
                if board[5] != " ":
                    return board[5]

            elif board[7]==board[8]==board[9]:
                if board[8] != " ":
                    return board[8]

        else:
            if turns < 9:
                return "play"
            else:
                return "draw"

   ###############################################################################   
    
    #executing
    while replay == "Y":
        
        #Welcome Screen
        print("Welcome to Tic Tac Toe!")
        print("Try lining up your characters horizontally, vertically, or diagonally to win!")
        print("Indicate placement location by using numbers ranging 1 to 9.")
        time.sleep(3)
        board = board_example
        display_board()
        print("The cell positions corresponding to numbers are shown above. Using a numpad is recommended.")
        board = board_clear
        player_order = input("Player 1, please choose X/O:").upper()
        if player_order == "X":
            print("Player 1 will go first!")
            player["X"] = "1"
            player["O"] = "2"
        else:
            print("Player 2 will go first!")
            player["X"] = "2"
            player["O"] = "1"
        print("Game will start in 3 seconds!")
        time.sleep(3)
        
        game_turns = 0
        player_order = "X"
        
        #Game session
        while goal == "play":
            game_turns += 1
            display_board()
            board_index = user_turn(player_order)
            board[board_index] = player_order
            if player_order == "X":
                player_order = "O"
            elif player_order == "O":
                player_order = "X"
            goal = goal_check(game_turns)
            #print(goal) #debugger
                   
        #Game over screen
        display_board()
        if goal == "X" or goal == "O":
            print("Player {} wins!".format(player[goal]))
        if goal == "draw":
            print("Draw!")
        
        #Resetting and replaying
        board = ["_", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        board_clear = ["_", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        goal = "play"
        #display_board() #debugger
        replay = input("Replay? Y/N").upper()

        clear_output()  
    return
    