class Workout:
    def __init__(self) -> None:  
      self.exercices=[]

    def add_exerice(self,m,n,r,w):
        new_exercice=Exercice(m,n,r,w)
        self.exercices.append(new_exercice)

    def show_exercices(self,athlete_name):
        print(f"{athlete_name}")
        for exo in self.exercices:
            print(f"  {exo.muscle}  ")
            print(f" {exo.name}    {exo.weight}kg * {exo.reps} ")

    def calculte_volume(self):
        print("workout_volume")
        volume=0
        for exo in self.exercices:
            volume+=exo.weight
        print(f"The total volume of the workout: {volume}")

    def strongest_exercice(self):
        print("Strongest exercice")
        max=self.exercices[0].weight * self.exercices[0].reps
        for exo in self.exercices:
            if exo.weight * exo.reps>max:
                max=exo.weight * exo.reps
        print(f"the max exrice is max: {max}")




class Exercice:
    def __init__(self,muscle,name,reps,weight) -> None:
        self.name=name
        self.reps=reps
        self.muscle=muscle
        self.weight=weight
GymObjcet=Workout()



def GymManager():
    print("Welcome to the gym manager")
    while True:
        print("""
            Add exercise
            Show history
            Calculate total volume
            Show strongest exercise
""")
        operation=(input("Choose betwenn those options "))
        if operation==1:
            muscle_name=input("Enter the name of the muslce you want to  target")
            exercice_name=input("Enter the name of the exercice")
            reps=input("Enter the number of reps")
            weight=input("Enter the Weight")
            GymObjcet.add_exerice(muscle_name,exercice_name,reps,weight)
        elif operation==2:
            athlete_name=input("Enter your name: ")
            GymObjcet.show_exercices(athlete_name)
        elif operation==3:
            GymObjcet.calculte_volume()
        elif operation==4:
            GymObjcet.strongest_exercice()
        else:
            break

        



