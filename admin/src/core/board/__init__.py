from ..board.issue import Issue


def list_issues():
    return Issue.query.all()
