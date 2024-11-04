import random

def demonstrate_random_functions():
    rand_float = random.random()
    print(f"Random float: {rand_float}")

    rand_int = random.randint(1, 10)
    print(f"Random integer between 1 and 10: {rand_int}")

    my_list = ["apple", "banana", "cherry", "date"]
    rand_choice = random.choice(my_list)
    print(f"Random choice from list: {rand_choice}")

    random.shuffle(my_list)
    print(f"Shuffled list: {my_list}")

    rand_sample = random.sample(my_list, 3)
    print(f"Random sample of 3 elements: {rand_sample}")

    rand_uniform = random.uniform(1.5, 5.5)
    print(f"Random uniform number between 1.5 and 5.5: {rand_uniform}")

if __name__ == "__main__":
    demonstrate_random_functions()
