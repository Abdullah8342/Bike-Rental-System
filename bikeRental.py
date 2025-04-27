import datetime
class BikeRental:
    def __init__(self,stock='0'):
        self.stock = stock

    def displaystock(self):
        print(f"We have currently {self.stock} bikes available to rent.")
        return self.stock

    def rent_bike(self,n,rental_type,charged):
        if n < 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} bikes available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            print(f"You have rented a {n} bike(s) on {rental_type} basis today at {now.hour} hours.")
            print(f"You will be charged ${charged} for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now

    def rentBikeOnHourlyBasis(self,n):
        return self.rent_bike(n,"hourly",5)

    def rentBikeOnDailyBasis(self,n):
        return self.rent_bike(n,"daily",20)

    def rentBikeOnWeeklyBasis(self,n):
        return self.rent_bike(n,"weekly",60)

    def returnBike(self,request):
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime

            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            if 3 <= numOfBikes <= 5:
                print("You are eligible for Family rental promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print(f"That would be ${bill}")
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:

    def __init__(self):
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestBike(self):
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
            return self.bikes

    def returnBike(self):
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes
        else:
            return 0,0,0
