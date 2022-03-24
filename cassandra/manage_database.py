from models.person_entity import PersonEntity
from models.location_entity import LocationEntity
from database.location_type import location
from database.person_model import person
from database.connection import Connection
import uuid
import datetime

class ManageFamilyTree:

    def __init__(self) -> None:
        connection = Connection()
        connection.createConnection()
        self.displayMenuOption = True

    def displayMenu(self):
        while self.displayMenuOption:
            print("====================MENU=========================")
            print("1 - List People")
            print("2 - See Details of a Person")
            print("3 - Add Person")
            print("4 - Add Parent")
            print("5 - Delete Person")
            print("0 - Exit")
            print("=================================================")
            response = input("Choose one option: ")

            if response == '0':
                self.displayMenuOption = False
            elif response == '1':
                self.listPeople()
            elif response == '2':
                self.seePersonDetails()
            elif response == '3':
                self.addPerson()
            elif response == '4':
                self.addParentToPerson()
            elif response == '5':
                self.deletePerson()
            else:
                print('Invalid option! Please, choose a valid option.')
                continue

    def listPeople(self):
        people = person.objects.all()
        print('============= LIST OF PEOPLE =============')
        for count, p in enumerate(people):
            print(f'{count} - {p.first_name} {p.last_name}')
        return people

    def findPersonById(self, id):
        return person.objects.filter(person_id=id)[0]
    
    def selectPerson(self, message="Select the person you want to work with: ") -> person:
        people = self.listPeople()
        index = int(input(message))
        return people[index]

    def seePersonDetails(self):
        p:person = self.selectPerson(f"Select the person you want to see the details: ")

        father = 'Not added yet'
        mother = 'Not added yet'
        
        if p.father_id is not None:
            f:person = self.findPersonById(p.father_id)
            if f is not None:
                father = f'{f.first_name} {f.last_name}'
        
        if p.mother_id is not None:
            m:person = self.findPersonById(p.mother_id)
            if m is not None:
                mother = f'{m.first_name} {m.last_name}'

        print('================= DETAILS ================')
        print(f'First Name    : {p.first_name}')
        print(f'Last Name     : {p.last_name}')
        print(f'Date Of Birth : {p.date_of_birth}')
        print(f"Place Of Birth: {p.place_of_birth['city']},{p.place_of_birth['state']} - {p.place_of_birth['country']}")
        print(f'Father : {father}')
        print(f'Mother : {mother}')

    def deletePerson(self):
        p:person = self.selectPerson(f"Select the person you want to delete: ")
        response = input("Are you sure you want to delete this person? y/n ")

        if response == 'y':
            try:
                p.timeout(None).delete()
                print(f'Person deleted!')
            except:
                print('Something went wrong while trying to delete this person!')


    def addParentToPerson(self):
        p:person = self.selectPerson(f"Select the person you want to add the parent to: ")
        parentOption = input('Do you want to add a (0) - father or  (1) - mother: ')
        try:
            parent:person = None
            response = input('Person already in the list? y/n ')
            if response == 'y':
                parent = self.selectPerson()
            else:
                parent = self.addPerson()
            if parentOption == '0':
                p.timeout(None).update(father_id=parent.person_id)
            else:
                p.timeout(None).update(mother_id=parent.person_id)
            print(f'{parent} added')
        except:
            print(f'Something went wrong while adding {parent}')

    
    def filterPeopleByName(self, name: str):
        for count, p in enumerate(person.objects.filter(first_name=name)):
            print(count, p.first_name, p.last_name)

    def getPersonInput(self) -> PersonEntity:
        first_name = input("First name: ")
        last_name = input("Last name: ")
        year = int(input("Year of Date of Birth: "))
        month = int(input("Month of Date of Birth: "))
        day = int(input("Day of Date of Birth: "))
        country = input("Country of Birth: ") 
        state = input("State of Birth: ") 
        city = input("City of Birth: ")

        person = PersonEntity(first_name=first_name, 
                                last_name=last_name, 
                                date_of_birth=datetime.datetime(year, month, day),
                                place_of_birth=LocationEntity(country, state, city))
        return person

    def addPerson(self):

        p = self.getPersonInput()
        try:
            person_created = person.create(person_id=uuid.uuid4(),
                            first_name=p.first_name, 
                            last_name=p.last_name, 
                            # date_of_birth=datetime.datetime(1994, 10, 20),
                            date_of_birth = p.date_of_birth,
                            place_of_birth=location(country=p.place_of_birth.country, state=p.place_of_birth.state, city=p.place_of_birth.city), 
                            father_id=None,
                            mother_id=None)
            return person_created
            
        except:
            print('Error when trying to add the person')
            return None

manager = ManageFamilyTree()
manager.displayMenu()

