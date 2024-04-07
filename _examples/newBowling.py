# This is to get a full game of bowling score.
# Author: Gordon Bosley
# Date 02/10/2019

def calcSumFor(first,second):
  return int(first) + int(second)

def total_score(score_sheet):
    score_sheet = score_sheet.replace('-', '0').split()
    bowScore = 0
    frame = 0
    print(score_sheet)
    while frame < 10:
        # How to handle strikes and the next two balls
        if score_sheet[frame][0] == 'X':
            bowScore = bowScore + 10
            if score_sheet[frame + 1][0] == 'X':   # one more than first
                bowScore = bowScore + 10
                if score_sheet[frame + 2][0] == 'X':
                        bowScore = bowScore + 10
                elif (score_sheet[frame + 2][0] != 'X') and (score_sheet[frame + 2][1] == '/'):
                    bowScore = calcSumFor(bowScore, (score_sheet[frame + 2][0]))
                elif (score_sheet[frame + 2][0] != 'X') and (score_sheet[frame + 2][1] != '/'):
                    bowScore = calcSumFor(bowScore, (score_sheet[frame + 2][0]))
            elif (score_sheet[frame + 1][0] != 'X') and (score_sheet[frame + 1][1] == '/'):
                bowScore = bowScore + 10
            else:
                bowScore = bowScore + calcSumFor((score_sheet[frame + 1][0]), (score_sheet[frame + 1][1]))
        # How to handle a spare and the next ball permutations
        elif score_sheet[frame][1] == '/':
            bowScore = bowScore + 10
            if score_sheet[frame + 1][0] == 'X':   # one more than first
                bowScore = bowScore + 10
            elif score_sheet[frame + 1][0] != 'X':
                bowScore = calcSumFor(bowScore, (score_sheet[frame + 1][0]))
        else:
            bowScore = bowScore + calcSumFor((score_sheet[frame][0]), (score_sheet[frame][1]))
        print(frame, ' ', score_sheet[frame], ' ', bowScore)
        frame += 1
    return bowScore

# Challenge input #1
score_sheet = 'X 7- 9- 8/  9/ X  X  X  X  35'
print("Bowler #1 score: ", total_score(score_sheet))
