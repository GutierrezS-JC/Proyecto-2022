from src.core.database import db

rol_permisos = db.Table(
    "rol_permisos",
    db.Column("rol_id", db.Integer, db.ForeignKey("roles.id"), primary_key=True),
    db.Column("permiso_id", db.Integer, db.ForeignKey("permisos.id"), primary_key=True),
)


class Rol(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(255))
    permisos = db.relationship("Permiso", secondary="rol_permisos")
