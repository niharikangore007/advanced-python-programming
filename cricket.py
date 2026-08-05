



class Player:
    

    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

        # Categorize player based on runs
        if self.runs >= 500:
            self.category = "Excellent"
        elif self.runs >= 200:
            self.category = "Good"
        else:
            self.category = "Average"

    def display(self):
        
        print(f"Player Name   : {self.player_name}")
        print(f"Jersey Number : {self.jersey_number}")
        print(f"Runs Scored   : {self.runs}")
        print(f"Category      : {self.category}")
        print("-" * 40)




class Team:


    def __init__(self):
        self.players = []

    def add_player(self, player):
        
        self.players.append(player)
        print(f"{player.player_name} added successfully!\n")

    def display_players(self):
      

        if len(self.players) == 0:
            print("No players available in the team.")
            return

        print("\n CRICKET TEAM DETAILS \n")

        for player in self.players:
            player.display()



team = Team()

# Creating Player Objects
p1 = Player("Virat Kohli", 18, 650)
p2 = Player("Rohit Sharma", 45, 480)
p3 = Player("Shubman Gill", 77, 180)
p4 = Player("KL Rahul", 1, 520)

# Adding Players to Team
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)
team.add_player(p4)

# Display All Player Details
team.display_players()