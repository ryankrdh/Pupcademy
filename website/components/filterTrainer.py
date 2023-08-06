from ..models import Trainer

trainer_names = [
    "Alex Smith",
    "Bella Mitchell",
    "Carter Green",
    "Daisy Campbell",
    "Ethan Foster",
    "Fiona Wright",
    "Grace Young",
    "Henry Adams",
    "Isabella Williams",
    "Jack James",
    "Kate Davis",
    "Liam Edwards",
    "Mia Irwin",
    "Noah Gray",
    "Olivia Davis",
    "Parker Fisher",
    "Quinn Fisher",
    "Riley Evans",
    "Sophia Young",
    "Tyler Wright",
    "Victoria Young",
    "William Edwards",
    "Xander Mitchell",
    "Yara Thomas",
    "Zachary Williams",
    "Amelia Clark",
    "Benjamin Foster",
    "Chloe Robinson",
    "Daniel Ramirez",
    "Ella Peterson",
    "Finn Green",
    "Gabriella Lewis",
    "Hannah Gray",
    "Isaac Phillips",
    "Julia Young",
    "Kevin Thomas",
    "Lily Clark",
    "Mason Evans",
    "Nora Foster",
    "Owen Phillips",
    "Penelope Wright",
    "Quinn Foster",
    "Riley Young",
    "Stella Gray",
    "Theodore Young",
    "Ursula Davis",
    "Violet Williams",
    "William Young",
    "Ximena Johnson",
    "Zoe Adams"
]



training_types = [
    "Obedience Training",
    "Therapy Training",
    "Behavioral Training",
    "Agility Training",
    "Protection Training",
    "Service Training",
    "Tracking Training"
]

sizes = [
    {"value": "small", "text": "Less than 22lbs"},
    {"value": "medium", "text": "22 - 57lbs"},
    {"value": "large", "text": "Greater than 57lbs"}
]

experiences = [
    {"value": "<5 YOE", "text": "Less than 5 years"},
    {"value": "5-10 YOE", "text": "5 - 10 years"},
    {"value": "10+ YOE", "text": "10+ years"}
]
cities = [
    "Seattle",
    "Spokane",
    "Tacoma",
    "Bellevue",
    "Kent",
    "Everett"
]

def fetch_filtered_trainers(training_type, size, experience, city):

    filter_query = Trainer.query

    if training_type:
        filter_query = filter_query.filter_by(training_type=training_type)

    if size:
        filter_query = filter_query.filter_by(size=size)

    if experience:
        filter_query = filter_query.filter_by(experience=experience)

    if city:
        filter_query = filter_query.filter_by(city=city)

    return filter_query.all()