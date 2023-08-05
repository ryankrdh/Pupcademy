# import random


# training_types = [
#     "Obedience Training",
#     "Therapy Training",
#     "Behavioral Training",
#     "Agility Training",
#     "Protection Training",
#     "Service Training",
#     "Tracking Training"
# ]

# sizes = [
#     {"value": "small", "text": "Less than 22lbs"},
#     {"value": "medium", "text": "22 - 57lbs"},
#     {"value": "large", "text": "Greater than 57lbs"}
# ]

# experiences = [
#     {"value": "less_than_5", "text": "Less than 5 years"},
#     {"value": "5_to_10", "text": "5 - 10 years"},
#     {"value": "10_plus", "text": "10+ years"}
# ]

# cities = [
#     "Seattle",
#     "Spokane",
#     "Tacoma",
#     "Bellevue",
#     "Kent",
#     "Everett"
# ]

# # Function to generate 50 fake dog trainer data objects
# def generate_fake_trainers():
#     fake_trainers = []
#     for _ in range(50):
#         name = f"Fake Trainer {_}"
#         training_type = random.choice(training_types)
#         size = random.choice(sizes)
#         experience = random.choice(experiences)
#         city = random.choice(cities)

#         trainer = Trainer(name=name, training_type=training_type, size=size, experience=experience, city=city)
#         fake_trainers.append(trainer)

#     return fake_trainers
