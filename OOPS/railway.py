import random

class Train:
    def __init__(Nod,TrainNo):
        Nod.TrainNo=TrainNo

    def book(Nod, fro, to):
        print(f"Congratulations.....")
        print(f"Your ticket {fro} to {to} is booked!!")

    def get_status(Nod):
        print(f"Train {Nod.TrainNo} is Running on time...")

    def fare(Nod,fro,to):
        print(f"Train number: {Nod.TrainNo} fare from {fro} to {to} is {random.randint(100,5000)}")

t = Train(12134)
t.get_status()
t.fare("Mumbai","Patna")
t.book("Mumbai","Patna")