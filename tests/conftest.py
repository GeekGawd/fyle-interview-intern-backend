import pytest
import json
from tests import app
from core.models.assignments import Assignment, AssignmentStateEnum
from core import db


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers

@pytest.fixture
def submitted_assignment():
    # Create a new assignment in the 'DRAFT' state
    assignment = Assignment.get_by_id(4)
    assignment.state = AssignmentStateEnum.SUBMITTED
    assignment.grade = None
    db.session.flush()

    yield assignment

    # Teardown (cleanup after the test runs)
    assignment.state = AssignmentStateEnum.DRAFT
    assignment.grade = None
    db.session.flush()

@pytest.fixture
def drafted_assignment():
    # Create a new assignment in the 'DRAFT' state
    assignment = Assignment.get_by_id(2)
    old_state = assignment.state
    old_grade = assignment.grade
    assignment.state = AssignmentStateEnum.DRAFT
    assignment.grade = None
    db.session.flush()

    yield assignment

    # Teardown (cleanup after the test runs)
    assignment.state = old_state
    assignment.grade = old_grade
    db.session.flush()