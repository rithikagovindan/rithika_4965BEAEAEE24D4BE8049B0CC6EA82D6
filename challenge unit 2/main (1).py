''' Implement a class called player that represents a cricket player.The Player class should have a
method  called play() which prints"The player is playing cricket.Derive two classes, Batsman and
Bowler, from the player class.override the play() methoy on each derived class to print batsman
is batting" and "The bowler is bowling", respectively.write a program to create object ofboth the
Batsman and Bowler classes and call the play() method for each object.'''


#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman (player):
  def play(self):
    print("The batsman in batting.")

#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is blowing.")

#create object of Batsmay and Bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play() method for each object 
batsman.play()
bowler.play()