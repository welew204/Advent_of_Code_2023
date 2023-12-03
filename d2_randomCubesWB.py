
def count_possible_games(games, possible_cubes):
    possible_red, possible_green, possible_blue = possible_cubes
    result = [] # list of possible games
    for idx, g in enumerate(games):
        possible = True
        g_id = idx+1
        g_runs = g.split(': ')[1]
        g_runs = g_runs.split('; ')
        for r in g_runs:
            data = r.split(', ')
            for d in data:
                d_list = d.split()
                color = d_list[1]
                number = int(d_list[0])
                if (color == 'green' and number > possible_green) \
                    or (color == 'red' and number > possible_red) \
                    or (color == 'blue' and number > possible_blue):
                    possible = False
                    break
            if possible == False:
                break
        if possible:
            result.append(g_id)

    return result

def min_cubes_needed(games):
    # for each game, determine min spanning set
    # reutrn the 'power' of each game
    res = []
    for idx, g in enumerate(games):
        min_green = 0
        min_red = 0
        min_blue = 0
        g_runs = g.split(': ')[1]
        g_runs = g_runs.split('; ')
        for r in g_runs:
            data = r.split(', ')
            for d in data:
                d_list = d.split()
                color = d_list[1]
                number = int(d_list[0])
                if color == 'green':
                    min_green = max(number, min_green)
                elif color == 'red':
                    min_red = max(number, min_red)
                elif color == 'blue':
                    min_blue = max(number, min_blue)
        power = min_green*min_red*min_blue
        res.append(power)
    
    return res

with open('/Users/williamhbelew/Hacking/AoC_2023/puzzle_inputs/d2_games.txt') as f:
    games = f.readlines()
    #print(sum(count_possible_games(games, (12, 13, 14))))
    print(sum(min_cubes_needed(games)))