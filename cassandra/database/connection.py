from cassandra.cqlengine import connection

class Connection:
    def createConnection(self):
        connection.setup(['127.0.0.1'], ['familytree'], protocol_version=3)
        connection.register_connection('Test Cluster', ['127.0.0.1'])
        connection.set_default_connection('Test Cluster')

# management.sync_type('cqlengine', location)
# management.sync_table(person)
