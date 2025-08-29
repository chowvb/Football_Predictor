PL_Teams = ["Arsenal", "Aston Villa", "Bournemouth","Brentford", "Brighton","Burnley","Chelsea","Crystal Palace", "Everton",
            "Fulham", "Leeds United", "Liverpool", "Manchester City", "Manchester United", "Newcastle", "Nottingham",
            "Sunderland", "Tottenham Hotspur", "West Ham", "Wolves"]
def validate_teams(home,away):
    if home in PL_Teams and away in PL_Teams:
        return 1
    else:
        return 2