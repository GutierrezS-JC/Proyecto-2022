from src.core.database import db

rol_permissions = db.Table(
    "rol_permissions",
    db.Column("rol_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
    db.Column("permission_id", db.Integer, db.ForeignKey("permissions.id"), primary_key=True),
)


class Rol(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    permissions = db.relationship("Permission", secondary=rol_permissions)
