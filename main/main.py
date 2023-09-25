from network import main as network
from voice import main as voice
from database import main as database

task = voice.listen()
database.insertin(task)

