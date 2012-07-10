#!/usr/bin/python

# -------------------------------------------------------------------
# Import statements
# -------------------------------------------------------------------
import sys

import sqlalchemy
from sqlalchemy.orm import relation

db = DatabaseConnection.DatabaseConnection()

# ========================
# Define database classes
# ========================
Base = db.Base

class User(Base):
	__tablename__ = 'user'
	__table_args__ = {'autoload' : True}

class Availability(Base):
	__tablename__ = 'availability'
	__table_args__ = {'autoload' : True}

class UserAvailability(Base):
	__tablename__ = 'user_availability'
	__table_args__ = {'autoload' : True}

class UserEvent(Base):
	__tablename__ = 'user_event'
	__table_args__ = {'autoload' : True}

class Event(Base):
	__tablename__ = 'event'
	__table_args__ = {'autoload' : True}

class Language(Base):
	__tablename__ = 'language'
	__table_args__ = {'autoload' : True}

class Expertise(Base):
	__tablename__ = 'expertise'
	__table_args__ = {'autoload' : True}

class Activity(Base):
	__tablename__ = 'activity'
	__table_args__ = {'autoload' : True}

class Audience(Base):
	__tablename__ = 'audience'
	__table_args__ = {'autoload' : True}

class UserAudience(Base):
	__tablename__ = 'user_audience'
	__table_args__ = {'autoload' : True}

class ActivityAudience(Base):
	__tablename__ = 'activity_audience'
	__table_args__ = {'autoload' : True}

class LanguageOffered(Base):
	__tablename__ = 'language_offered'
	__table_args__ = {'autoload' : True}

class EventLanguage(Base):
	__tablename__ = 'event_language'
	__table_args__ = {'autoload' : True}

class ExpertiseOffered(Base):
	__tablename__ = 'expertise_offered'
	__table_args__ = {'autoload' : True}

class ExpertiseSought(Base):
	__tablename__ = 'expertise_sought'
	__table_args__ = {'autoload' : True}

class ActivityOffered(Base):
	__tablename__ = 'activity_offered'
	__table_args__ = {'autoload' : True}

class ActivitySought(Base):
	__tablename__ = 'activity_sought'
	__table_args__ = {'autoload' : True}


# -------------
# Relationships
# -------------


# ---------------------------------------------------------
# Test that all relationships/mappings are self-consistent.
# ---------------------------------------------------------
from sqlalchemy.orm import compile_mappers
try:
	compile_mappers()
except RuntimeError, error:
	print """
An error occurred when verifying the relationships between the database tables.
Most likely this is an error in the definition of the SQLAlchemy relationships - 
see the error message below for details.
"""
	print "Error type: %s" % sys.exc_info()[0]
	print "Error value: %s" % sys.exc_info()[1]
	print "Error trace: %s" % sys.exc_info()[2]
	sys.exit(1)
