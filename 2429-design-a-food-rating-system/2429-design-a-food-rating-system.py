class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_to_info = {}  # food -> (cuisine, rating)
        self.cuisine_to_foods = {}  # cuisine -> SortedList of (-rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_info[food] = (cuisine, rating)
            if cuisine not in self.cuisine_to_foods:
                self.cuisine_to_foods[cuisine] = SortedList()
            self.cuisine_to_foods[cuisine].add((-rating, food))

    def changeRating(self, food, newRating):
        cuisine, oldRating = self.food_to_info[food]
        self.cuisine_to_foods[cuisine].remove((-oldRating, food))
        self.cuisine_to_foods[cuisine].add((-newRating, food))
        self.food_to_info[food] = (cuisine, newRating)

    def highestRated(self, cuisine):
        return self.cuisine_to_foods[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)