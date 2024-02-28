# from DungeonAdventure import DungeonAdventure
import pickle

class SaveGame:

    #save during the game, after user beats the monsters or something big
    #timer, every 30 seconds save game, feedback to user

    def pickle(self, da_game):
        """
        Saves the Dungeon Adventure game as a pickle file
        """
        with open('dungeon_adventure.pickle', 'wb') as saved_file:
            pickle.dump(da_game, saved_file)

# game = SaveGame()
# game.run_all()

