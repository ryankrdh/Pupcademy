# from . import db
# from models import Trainer
# from .trainerAssets import generate_fake_trainers

# def generate_and_populate_trainers():
#     # Check if trainers already exist in the database, if not, generate them
#     if not Trainer.query.first():
#         fake_trainers = generate_fake_trainers()

#         for trainer in fake_trainers:
#             db.session.add(trainer)

#         db.session.commit()
