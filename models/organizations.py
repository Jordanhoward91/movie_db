from sqlalchemy.dialects.postgresql import UUID
import uuid
import marshmallow as ma

from db import db

class Organizations(db.Model):
  __tablename__ = "organizations"
  org_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
  name = db.Column(db.String(), nullable = False)
  phone = db.Column(db.String(), nullable = False)
  city = db.Column(db.String(), nullable = False)
  state = db.Column(db.String(), nullable = False, unique = True)
  active = db.Column(db.String(), nullable = False, unique = False)
  users = db.relationship('AppUsers', cascade="all,delete", backref = 'organization', lazy=True)

  def __init__(self, name, phone, city, state, active = True):
    self.name = name
    self.phone = phone
    self.city = city
    self.state = state
    self.active = active

class OrganizationsSchema(ma.Schema):
  class Meta:
    fields = ['org_id', 'name', 'phone', 'city', 'state', 'active']

organization_schema = OrganizationsSchema()
organizations_schema = OrganizationsSchema(many=True)

