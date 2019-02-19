import ijson
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from elios_app.models import Base, Person, Address, CriminalRecord
from database import engine
from enum import Enum
import math

# Connect to Database
Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
session = sessionmaker(bind=engine)()

class Severity(Enum):
    VERY_HIGH = 100
    HIGH = 75
    MEDIUM = 50
    LOW = 25
    VERY_LOW = 10

class Weight(Enum):
    SOCIAL_MEDIA = 0.1  # 10 percent
    EMAIL = 0.1         # 10 percent
    PHONE = 0.025       # 2.5 percent
    CRIMINAL_RECORD = 0.4   # 40 percent
    CIVIL = 0.3             # 30 percent
    PROPERTIES = 0.05       # 5 percent
    ADDRESSES = 0.025       # 2.5 percent

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
                risk_score = calculate_risk_score(row),
                has_criminal_record = len(row['criminal']['criminal']) > 0
            )

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
    print("Parsing complete")


def calculate_risk_score(row ):
    risk_score = 0

    risk_score += len(row['emails']) * Severity.MEDIUM.value * Weight.EMAIL.value
    risk_score += len(row['phone_numbers']) * Severity.VERY_LOW.value * Weight.PHONE.value
    risk_score += len(row['social_media']) * Severity.MEDIUM.value * Weight.SOCIAL_MEDIA.value
    risk_score += len(row['properties']) * Severity.LOW.value * Weight.PROPERTIES.value
    risk_score += len(row['addresses']) * Severity.LOW.value * Weight.ADDRESSES.value
    risk_score += sum_criminal_record_points(row['criminal']['criminal']) * Severity.VERY_HIGH.value * Weight.CRIMINAL_RECORD.value
    risk_score += sum_civil_suit_points(row['court']) * Severity.HIGH.value * Weight.CIVIL.value

    
    return math.ceil(risk_score)


def sum_criminal_record_points(records):
    points = 0
    for rec in records:
        if (rec['Disposition'].lower() == 'sentenced') or ('found guilty' in rec['Disposition'].lower()):
            points+=2
        else:
            points+=1
    return points


def sum_civil_suit_points(records):
    points = 0
    for rec in records:
        if (rec['disposition'] is None) or ('dismissed' in rec['disposition'].lower()): continue
        # Resulted in Debt (Consent Judgement)
        if 'consent' in rec['disposition'].lower():
            points += 2
        # Debt was discharged
        elif 'standard discharge' in rec['disposition'].lower():
            points += 1
    return points


def main():
    parse()


if __name__ == '__main__':
    main()