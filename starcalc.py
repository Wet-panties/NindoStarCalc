

def definestage(stage):
    rankstage = {'A': 1, 'A+': 2, 'S-': 3, 'S': 4, 'S+': 5}
    for i in rankstage:
        if stage == i:
            stage = rankstage[i]
            return stage
        else:
            pass


def maxstars(stage):
    stagestar = {1: 5, 2: 9, 3: 12, 4: 13, 5: 14}
    for i in stagestar:
        if stage == i:
            stage = stagestar[i]
            return stage
        else:
            pass

    pass


rank: str = input('char rank? (A - S+): ')
userstage = definestage(rank)
userstar = maxstars(userstage)
print(f'Maximum stars: {userstar}')





