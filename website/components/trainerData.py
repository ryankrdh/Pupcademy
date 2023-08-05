
# from models import Trainer, db
# from .trainerAssets import DogTrainer, training_types, sizes, experiences, cities
# import random

# # Function to generate random trainers and add them to the database
# def generate_fake_trainers(num_trainers=50):
#     for _ in range(num_trainers):
#         name = f"Fake Trainer {_}"
#         training_type = random.choice(training_types)
#         size = random.choice(sizes)["value"]
#         experience = random.choice(experiences)["value"]
#         city = random.choice(cities)

#         # Create a new trainer object and add it to the database
#         new_trainer = Trainer(name=name, training_type=training_type, size=size, experience=experience, city=city)
#         db.session.add(new_trainer)
    
#     db.session.commit()

# generate_fake_trainers(50)
