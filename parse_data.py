import ijson
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from elios_app.models import Base, Person, Address, CriminalRecord
from database import engine

# Connect to Database
Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
session = sessionmaker(bind=engine)()

def parse():
    # Ensure tables are empty first
    session.query(Person).delete()
    session.query(CriminalRecord).delete()
    session.query(Address).delete()
    print("DB emptied")

    filename = "exercise.json"
    print("Opening %s for parsing" % filename)
    
    with open(filename, 'r') as json_input:
        objects = ijson.items(json_input, 'item')
        for row in objects:
            new_person = Person(
                first_name  = row['fname'],
                middle_name = row['mname'],
                last_name   = row['lname'],
                date_of_birth = row['dob'], 
                full_name = "%s %s %s" % (row['fname'], row['mname'], row['lname']),
                risk_score = 0,
                has_criminal_record = len(row['criminal']['criminal']) > 0
            )

            new_person.risk_score = calculate_risk_score()

            ## Save person
            session.add(new_person)
            session.commit()

            ## Get person addresses
            for addr in row['addresses']:
                address = Address(
                    person = new_person,
                    street = addr['street'],
                    city = addr['city'],
                    state = addr['state'],
                    zipcode = addr['zipcode'],
                    type = addr['type'],
                    time = addr['time'],
                    value = addr['value']
                )
                ## Save Address
                session.add(address)
                session.commit()


                # print(address.person_id)
                # print(address.street)
                # print(address.city)
                # print(address.state)
                # print(address.zipcode)
                # print(address.type)
                # print(address.time)
                # print(address.value)
                # print("\n")

            ## Get person's criminal records
            for rec in row['criminal']['criminal']:
                record = CriminalRecord(
                    person = new_person,
                    first_name = rec['firstname'],
                    middle_name = rec['middlename'],
                    last_name = rec['lastname'],
                    race = rec['race'],
                    date_of_birth = rec['dob'],
                    address = rec['address'],
                    address_second_line = rec['address2'],
                    city = rec['city'],
                    state = rec['state'],
                    zip = rec['zip'],
                    case_number = rec['casenumber'],
                    charge_category = rec['ChargeCategory'],
                    charges_filed_date = rec['ChargesFiledDate'],
                    offense_date = rec['OffenseDate'],
                    offense_code = rec['OffenseCode'],
                    offense_description = rec['offensedescription1'],
                    counts= rec['Counts'],
                    plea = rec['Plea'],
                    conviction_date = rec['ConvictionDate'],
                    conviction_place= rec['ConvictionPlace'],
                    court = rec['court'],
                    source = rec['source'],
                    sentence_date = rec['SentenceYYYMMDDD'],
                    probation_date = rec['ProbationYYYMMDDD'],
                    disposition = rec['Disposition'],
                    disposition_date = rec['Dispositiondate'],
                    arresting_agency = rec['ArrestingAgency'],
                    case_type= rec['caseType'],
                    fines= rec['Fines'],
                    source_name = rec['SourceName'],
                    source_state = rec['SourceState'],
                    mugshot = rec['mugshot'],
                )

                ## Save Criminal Record
                session.add(record)
                session.commit()

                # print(record.__dict__.keys())
                # for r in record.__dict__:
                    # print("%s: %s" % (r, record.__dict__[r]))
            # print(obj['fname'])
            # print(obj['mname'])
            # print(new_person.risk_score)
            # print(new_person.has_criminal_record)
            
            # print(type(obj['criminal']))
            # print(obj['criminal']['criminal'])
            # print("\n")
    print("Parsing complete")

def calculate_risk_score():
    return 5

def main():
    print("hello, world")
    parse()

if __name__ == '__main__':
    main()