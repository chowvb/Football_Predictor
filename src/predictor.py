def predict_match(home, away):
    from src.validate.validate_TeamNames import validate_teams
        
    if validate_teams(home,away)==1:
        win = 33
        draw = 33
        loss = 33
        return print(f"{win}/{draw}/{loss}")
    else:
        return print("Invalid Team name entered")

team1 = "Liverpool"
team2 = "Manchester United"
predict_match(team1, team2)