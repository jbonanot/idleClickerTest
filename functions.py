def scoreUp():
    global scoreValue
    global scoreBox
    scoreValue = scoreValue + 1
    scoreBox["text"] = "Score: " + str(scoreValue)
