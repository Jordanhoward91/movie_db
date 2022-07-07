from re import L
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import marshmallow as ma

from db import db
from models import organizations

from models.organizations import OrganizationsSchema

class AppUsers(db.Model):
  __tablename__="users"
  user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  first_name = db.Column(db.String(), nullable = False)
  last_name = db.Column(db.String(), nullable = False)
  email = db.Column(db.String(), nullable = False, unique = True)
  password = db.Column(db.String(), nullable = False)
  city = db.Column(db.String())
  state = db.Column(db.String())
  active = db.Column(db.Boolean(), nullable=False, default=False)
  org_id = db.Column(UUID(as_uuid=True), db.ForeignKey('organizations.org_id'), nullable=False)
  created_date = db.Column(db.DateTime, default=datetime.utcnow)
  role = db.Column(db.String(), default='user', nullable=False)

  def __init__(self, first_name, last_name, email, password, city, state, role, org_id):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.city = city
    self.state = state
    self.active = True
    self.org_id = org_id
    self.role = role

class AppUsersSchema(ma.Schema):
  class Meta:
    fields = ['user_id', 'first_name', 'last_name', 'email', 'phone', 'city', 'created_date', 'role', 'active', 'org_id']

  organizations = ma.fields.Nested(OrganizationsSchema(only=("name", "active")))

user_schema = AppUsersSchema()
users_schema = AppUsersSchema(many=True)