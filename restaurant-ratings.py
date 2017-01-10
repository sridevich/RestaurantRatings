# your code goes here
restaurant_ratings_file = open ("scores.txt")
restaurant_ratings_dict = {}

def make_ratings_dict(restaurant_ratings_file):
    for line in restaurant_ratings_file:
        line = line.rstrip()
        restaurant_name, restaurant_rating  = line.split(":")
        restaurant_ratings_dict[restaurant_name] = restaurant_rating

def print_ratings_dict(restaurant_ratings_dict):
    for restaurant, rating in sorted(restaurant_ratings_dict.items()):
        print " %s is rated  %s." % (restaurant,  rating)

make_ratings_dict(restaurant_ratings_file)
print_ratings_dict(restaurant_ratings_dict)
