# __author__ = 'anna'
# Not finished
# import games
#
# class Tr_location(object):
#     CITIES = ["New York", "San Francisco", "San Mateo", "Sunnyvale"]
#     COUNTRIES = ["USA"]
#
#     def __init__(self, city, country):
#         self.city = city
#         self.county = country
#
#
#     def __str__(self):
#         rep = self.city + "," +self.county
#         return rep
#
# class Tr_loc_list(object):
#
#     def __init__(self):
#         self.list = []
#
#     def __str__(self):
#         if self.list:
#             rep = ""
#             for location in self.list:
#                 rep += str(location) + "\t"
#         else:
#             rep = "<empty>"
#         return rep
#
#     def add(self, location):
#         self.list.append(location)
#
#     def clear(self):
#         self.list = []
#
#     def populate(self):
#         for country in Tr_location.COUNTRIES:
#             for city in Tr_location.CITIES:
#                 self.add(Tr_location(city,country))
#
#
# class Tr_player(object):
#
#     def __init__(self, name, location = "Home"  ):
#         self.name = name
#         self.location = location
#
#     def __str__(self):
#         rep = self.name + "," + self.location
#         return rep
#
#     def travel(self, location):
#         self.location = location
#
# class Tr_game(object):
#     """ A Travel game. """
#     def __init__(self):
#         self.name = Tr_player.name
#         self.Tr_loc_list = Tr_loc_list
#         self.Tr_loc_list.populate()
#
#     def play(self):
#         choice = games.ask_number("Choose a number assigned to place you want to travel:", low = 0, high = len(self.Tr_loc_list))
#
#     def main(self):
#
#         print("""Welcome to the travel game!
#         Here are the list or locations:
#               """)
#         name = input("Enter player name:")
#         player = Tr_player(name)
#         num = 0
#         for loc in self.Tr_loc_list:
#             num += 1
#             print(location, "-", num)
#
#
#
