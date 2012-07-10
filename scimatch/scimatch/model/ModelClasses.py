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

class CamelCase(Base):
	__tablename__ = 'camel_case'
	__table_args__ = {'autoload' : True}

class Table2(Base):
	__tablename__ = 'table2_name'
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
