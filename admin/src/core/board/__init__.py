from src.core.database import db
from src.core.board.permiso import Permiso
from src.core.board.rol import Rol
from src.core.board.config import Config


# def list_issues():
#     return Issue.query.all()
#
#
# def create_issue(**kwargs):
#     issue = Issue(**kwargs)
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue
#
#
# def assign_user(issue, user):
#     issue.user = user
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue
#
#
# def assign_labels(issue, labels):
#     issue.labels.extend(labels)
#     db.session.add(issue)
#     db.session.commit()
#
#     return issue
#
#
# def create_label(**kwargs):
#     label = Label(**kwargs)
#     db.session.add(label)
#     db.session.commit()
#
#     return label

def get_rol_by_id(rol_id):
    return Rol.query.get(rol_id)
