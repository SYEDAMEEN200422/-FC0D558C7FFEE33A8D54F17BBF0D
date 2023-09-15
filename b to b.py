class player:
  def play(self):
    print("the player play cricket")

class Batsman(player):
  def play(self):
    print("the batsman is bating")

class Bowler(player):
  def play(self):
    print("the bowlwer is bowling")

batsman = Batsman()
bowler = Bowler()

batsman.play() 
bowler.play()