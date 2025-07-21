import random
import seaborn as sns

class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 36) if i % 2 == 0]
        self.dumbbell_holder = {}
        self.restart_the_day()
        
    def restart_the_day(self):
        self.dumbbell_holder = {i: i for i in self.dumbbells}
    
    def list_dumbbells(self):
        return [i for i in self.dumbbell_holder.values() if i != 0]
    
    def list_available_spaces(self):
        return [i for i, j in self.dumbbell_holder.items() if j == 0]
    
    def pick_up_dumbbell(self, dumbbell):
        dumbbell_position = list(self.dumbbell_holder.values()).index(dumbbell)
        dumbbell_key = list(self.dumbbell_holder.keys())[dumbbell_position]
        self.dumbbell_holder[dumbbell_key] = 0
        return dumbbell
    
    def return_dumbbell(self, pos, dumbbell):
        self.dumbbell_holder[pos] = dumbbell
            
    def calculate_chaos(self):
        num_chaos = [i for i, j in self.dumbbell_holder.items() if i != j]
        return len(num_chaos) / len(self.dumbbell_holder)

class User():
    def __init__(self, user_type, gym):
        self.user_type = user_type # 1 - normal | 2 - Messy
        self.gym = gym
        self.dumbbell = 0
    
    def start_training(self):
        list_of_available_dumbbells = self.gym.list_dumbbells()
        self.dumbbell = random.choice(list_of_available_dumbbells)
        self.gym.pick_up_dumbbell(self.dumbbell)
    
    def finish_training(self):
        available_spaces = self.gym.list_available_spaces()

        if not available_spaces:
            return

        if self.user_type == 1:
            if self.dumbbell in available_spaces:
                self.gym.return_dumbbell(self.dumbbell, self.dumbbell)
            else:
                pos = random.choice(available_spaces)
                self.gym.return_dumbbell(pos, self.dumbbell)
        else: # Messy user (user_type == 2)
            pos = random.choice(available_spaces)
            self.gym.return_dumbbell(pos, self.dumbbell)

        self.dumbbell = 0
            
if __name__ == '__main__':
    gym = Gym()
    
    users = [User(1, gym) for i in range(10)]
    users += [User(2, gym) for i in range(1)] 
    random.shuffle(users)
    
    list_chaos = []
    
    for k in range(50):
        gym.restart_the_day()
        for i in range(10):
            random.shuffle(users)
            
            for user in users:
                user.start_training()
            for user in users:
                user.finish_training()
        list_chaos += [gym.calculate_chaos()]
    
    sns.displot(list_chaos)