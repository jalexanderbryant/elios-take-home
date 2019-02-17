from sqlalchemy import Column 
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(64))
    middle_name = Column(String(64))
    last_name = Column(String(64))
    full_name = Column(String(64))
    date_of_birth = Column(String(64))
    has_criminal_record = Column(Boolean, nullable=False)
    risk_score = Column(Integer, nullable=False)

    @property
    def serialize(self):
        """Return serialized data for User"""
        return {
            'id': self.id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'date_of_birth': self.date_of_birth,
            'risk_score': self.risk_score,
            'has_criminal_record': self.has_criminal_record,
        }

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))
    zipcode = Column(String(10))
    type = Column(String(32))
    time = Column(String(32))
    value = Column(Integer)

    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return serialized data for Address"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode,
            'type': self.type,
            'time': self.time,
            'value': self.value
        }

class CriminalRecord(Base):
    __tablename__ = 'criminal_record'

    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer, ForeignKey('user.id'))

    first_name = Column(String(64))
    middle_name =Column(String(64))
    last_name = Column(String(64))
    race = Column(String(64))
    date_of_birth = Column(String(64))
    address = Column(String(64))
    address_second_line = Column(String(64))
    city= Column(String(64))
    state= Column(String(64))
    zip= Column(Integer)
    case_number= Column(String(64))
    charge_category= Column(String(64))
    charges_filed_date= Column(String(64))
    offense_date= Column(String(64))
    offense_code= Column(String(64))
    offense_description= Column(String(64))
    counts= Column(Integer)
    plea= Column(String(64))
    conviction_date= Column(String(64))
    conviction_place= Column(String(64))
    court= Column(String(64))
    source= Column(String(64))
    sentence_date= Column(Integer)
    probation_date= Column(Integer)
    disposition= Column(String(64))
    disposition_date= Column(String(64))
    arresting_agency= Column(String(64))
    case_type= Column(String(64))
    fines= Column(String(64))
    source_name= Column(String(64))
    source_state= Column(String(64))
    mugshot= Column(String(250))

    @property
    def serialize(self):
        """Return serialized data for Criminal Record"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "first_name": self.first_name,
            "middle_name": self.middle_name,
            "last_name": self.last_name,
            "full_name": self.full_name,
            "race": self.race,
            "date_of_birth": self.date_of_birth,
            "address": self.address,
            "address_second_line": self.address_second_line,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "case_number": self.case_number,
            "charge_category": self.charge_category,
            "charges_filed_date": self.charges_filed_date,
            "offense_date": self.offense_date,
            "offense_code": self.offense_code,
            "offense_description": self.offense_description,
            "counts": self.counts,
            "plea": self.plea,
            "conviction_date": self.conviction_date,
            "conviction_place": self.conviction_place,
            "court": self.court,
            "source": self.source,
            "sentence_date": self.sentence_date,
            "probation_date": self.probation_date,
            "disposition": self.disposition,
            "disposition_date": self.disposition_date,
            "arresting_agency": self.arresting_agency,
            "case_type": self.case_type,
            "fines": self.fines,
            "source_name": self.source_name,
            "source_state": self.source_state,
            "mugshot": self.mugshot,
        }