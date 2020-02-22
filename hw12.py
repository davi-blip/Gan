import tkinter as tk
import random

#Extra credit part 1

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,classes):
        classes = classes.split(',')
        self.number = classes[0]
        self.name = classes[1]
        self.rate = classes[2]
        self.speed = classes[3]

    def __repr__(self):
        return str(self.name)

    def caught_rate(self):
        num = min(int(self.rate)+1,151)
        return (num / 449.5)

    def run_rate(self):
        return ((2*int(self.speed))/256)



#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
    def __init__(self, master=None):
        self.pokemons = []
        self.current_pokemon = None
        with open('pokedex.csv') as f:
            for lines in f:
                pokemon = Pokemon(lines)
                self.pokemons.append(pokemon)

        self.balls = 50
        self.caught_pokemon = []
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        self.pack()
        self.createWidgets()

        #Call nextPokemon() method here to initialize your first random pokemon
        self.nextPokemon()

    def createWidgets(self):
        #See the image in the instructions for the general layout required
        #"Run Away" button has been completed for you as an example:
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball"+'('+str(self.balls)+' '+"left"+')'
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack()
        
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack()

        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="white")
        self.messageLabel.pack(fill="x", padx=5, pady=5)

        #Complete and pack the pokemonImageLabel here.

        self.image_label = tk.Label()
        self.image_label.pack()
    
        #Complete and pack the catchProbLabel here.
        self.catchProbLable = tk.Label(bg="white")
        self.catchProbLable.pack()

        self.runProbLable = tk.Label(bg = "white")
        self.runProbLable.pack()


    def nextPokemon(self):
        self.current_pokemon = random.choice(self.pokemons)
        self.messageLabel["text"]="You encounter a wild" + ' '+self.current_pokemon.name
        self.image = tk.PhotoImage(file="sprites/"+str(self.current_pokemon.number)+".gif")
        self.image_label["image"] = self.image
        self.catchProbLable["text"]="Your chance of catching it is" + ' '+ str(self.current_pokemon.caught_rate())
        self.runProbLable["text"]="Chance of running away" +' '+ str(self.current_pokemon.run_rate())

        
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
        
    def throwBall(self):
        num_rate = random.random()
        if num_rate < self.current_pokemon.caught_rate():
            self.caught_pokemon.append(self.current_pokemon.name)
            self.nextPokemon()
        elif num_rate < self.current_pokemon.run_rate():
            self.messageLabel["text"]="Aargh! It escaped!"
            self.update()
            self.after(500)
            self.nextPokemon()

                  
        if self.balls > 0:
            self.balls -= 1
            self.throwButton["text"]="Throw Safari Ball"+'('+str(self.balls)+' '+"left"+')'
        else:
            self.endAdventure()

        
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
        
    def endAdventure(self):
        self.image_label.pack_forget()
        self.throwButton.pack_forget()
        self.runButton.pack_forget()
        self.runProbLable.pack_forget()
        self.messageLabel["text"]="You're out of balls, I hope you had fun!"
        a="You caught"+' '+str(len(self.caught_pokemon))+' '+"Pokemon:" +'\n'
        for i in self.caught_pokemon:
            a += i+'\n'
        self.catchProbLable["text"]= a
        
        
        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()
