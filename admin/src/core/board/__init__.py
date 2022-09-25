from ..board.issue import Issue
from ..database import db


def list_issues():
    return Issue.query.all()


def create_issue(**kwargs):
    issue = Issue(**kwargs)
    db.session.add(issue)
    db.session.commit()
