from cassandra.cqlengine import columns
from cassandra.cqlengine.usertype import UserType

class location(UserType):
    country = columns.Text()
    state = columns.Text()
    city = columns.Text()