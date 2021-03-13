def game():
    return 554

score = game()
with open("high_score.txt") as f:
    highscore = int(f.read())

if score>highscore:
    with open("high_score.txt","w") as f:
        f.write(str(score))

# ya Sara ma na apni taraf sa likha ha
    
if score>highscore:
    with open("high_score.txt") as f:
        content = f.read()
        print(f"Congratulation! You Scored High {content} then the Previous one ")
elif score==highscore:
    print("You Equal the Previous High SCore")
else:
    print(f"Your Score {score} is less then the Previous High score , Previous High Score is {highscore}")
