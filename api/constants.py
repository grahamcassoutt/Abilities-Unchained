from enum import Enum

USER_PASSWORD = "GottaGetThatData!"
DATABASE_NAME = "Abilities-Unchained"
DB_URI = 'mongodb+srv://JMarch12:GottaGetThatData!@abilities-unchained.5mrctok.mongodb.net/?retryWrites=true&w=majority'

class RelationshipStatus(Enum):
    FRIENDS = 1
    PENDING = 2
    NO_RELATIONSHIP = 3