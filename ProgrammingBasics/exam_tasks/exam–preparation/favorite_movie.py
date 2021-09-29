movie=input()
num_movies=0
best_movie=''
max_points=0

while movie!='STOP':
    points_for_movie = 0
    num_movies+=1
    for letter in movie:
        if 65<=ord(letter)<=90:
            points=ord(letter)-len(movie)
        elif 97<=ord(letter)<=122:
            points=ord(letter)-2*len(movie)
        else:
            points=ord(letter)
        points_for_movie+=points
    if points_for_movie>max_points:
        max_points=points_for_movie
        best_movie=movie
    if num_movies==7:
        break
    movie = input()

if num_movies==7:
    print('The limit is reached.')

print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')



