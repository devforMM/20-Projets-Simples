class MovieManager:
    def __init__(self) -> None:
        self.movies=[]
    def add_movie(self,movie_name,gender):
        movie=Movie(
            movie_name,
            gender
        )
        self.movies.append(movie)
        print("The Movie was added succesfully")
    def rate_movie(self,movie_name,rating):
        for movie in self.movies:
            if movie.title==movie_name:
                movie.rating=rating
        print("The movie was succesfully rated")
        
    def best_movies(self):
        movies_rating=[(m.title,m.rating) for m in self.movies]
        results=sorted(movies_rating,key=lambda x:x[1])
        for r in results:
            print(f"{r[0]}   {r[1]}")
        
    def delete_movie(self,movie_title):
        target_movie=None
        for m in self.movies:
            if m==movie_title:
                target_movie==m
        self.movies.remove(target_movie)
        print("the movie was succesfully removed")
    
    def search_movie(self,title):
        target_movie=None
        for movie in self.movies:
            if movie.title==title:
                target_movie=movie
        if target_movie:
            print(f" Movie informations  Title: {target_movie.title}  Gender: {target_movie.gender}  Rating: {target_movie.rating}")
        else:
            print("no correspanding movie for your search")
    def movies_by_gender(self):
        dictionnaire={}
        for m in self.movies:
            if m.gender in dictionnaire.keys():
                dictionnaire[m.gender].append(m.title)
            else:
                dictionnaire[m.gender]=[m.title]

        for k,v in dictionnaire.items():
            print(f"movies of : {k}")
            for title in dictionnaire[k]:
                print(f"Title:{title} ")
    



class Movie:
    def __init__(self,title,gender) -> None:
        self.title=title
        self.rating=0
        self.gender=gender



movie_manager=MovieManager()
def movies_system():
    print("welcom to movies manager")
    while True:
        print("""Select an option :
                Add movie
                Search movie
                Rate movie
                Show best movies
                Show movies by genre
                Delete movie
        """)
        operation=int(input("Chose an operation betwwen the operations: "))
        if operation==1:
            movie_name=input(f"Enter the movie title: ")
            gender=input(f"Enter the movie gender: ")
            movie_manager.add_movie(movie_name,gender)
        elif operation==2:
            movie_name=input(f"Enter the movie title: ")
            movie_manager.search_movie(movie_name)
        elif operation==3:
            movie_name=input(f"Enter the movie title: ")
            rating=input("Enter your rating for the movie: ")
            movie_manager.rate_movie(movie_name,rating)
        elif operation==4:
            movie_manager.best_movies()
        elif operation==5:
            movie_manager.movies_by_gender()
        elif operation==6:
            movie_name=input(f"Enter the movie title: ")
            movie_manager.delete_movie(movie_name)
        else:
            break
