game = False # Не играем
max_total = 100
total = max_total

def get_total():
    global total
    return total

def take_candies(take: int):
    global total
    total -= take

def set_max_total(value: int):
    global max_total
    max_total = value
    

def check_game():
    global game
    return game

def new_game():
    global game
    global total
    if game:
        game = False
    else:
        total = max_total
        game = True
        


        
        


        
