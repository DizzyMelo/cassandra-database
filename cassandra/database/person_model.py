from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from database.location_type import location

class person(Model):
    __keyspace__ = 'familytree'
    __connection__ = 'Test Cluster'
    person_id = columns.UUID(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
    place_of_birth = columns.UserDefinedType(location)
    date_of_birth = columns.Date()
    father_id = columns.UUID()
    mother_id = columns.UUID()
