import random
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.students import Student
from core.models.teachers import Teacher
from core.libs.helpers import get_utc_now
from sqlalchemy.orm import Session
from core import db

# def create_fake_assignment(session: Session, student_id: int, teacher_id: int, state: AssignmentStateEnum):
#     """Create a fake assignment."""
#     # Create a new Assignment instance
#     assignment = Assignment(
#         student_id=student_id,
#         teacher_id=teacher_id,
#         content="New Assugnisifiofdoifd",
#         grade=None,  # Grade is None initially
#         state=AssignmentStateEnum.DRAFT,  # State is randomly chosen
#         created_at=get_utc_now(),
#         updated_at=get_utc_now(),
#     )

#     # Add the new assignment to the session
#     session.add(assignment)

#     # Commit the session to save the assignment to the database
#     session.commit()

#     return assignment

# def create_fake_assignments(session: Session):
#     # Fetch all student and teacher IDs
#     student_ids = [student.id for student in session.query(Student.id).all()]
#     teacher_ids = [teacher.id for teacher in session.query(Teacher.id).all()]

#     # Fetch all possible states
#     states = list(AssignmentStateEnum)

#     # For each student, create a fake assignment with a random teacher and state
#     for i in range(10):
#         student_id = random.choice(student_ids)
#         teacher_id = random.choice(teacher_ids)
#         state = random.choice(states)
#         create_fake_assignment(session, student_id, teacher_id, state)

# # Usage:
# create_fake_assignments(db.session)

from core.models.assignments import Assignment, AssignmentStateEnum

def submit_assignment(assignment_id):
    # Fetch the assignment by id
    assignment = Assignment.get_by_id(assignment_id)

    # Check if the assignment exists and is in the 'DRAFT' state
    if assignment and assignment.state == AssignmentStateEnum.GRADED:
        # Update the state to 'SUBMITTED'
        assignment.state = AssignmentStateEnum.DRAFT
        assignment.grade = None
        db.session.commit()
        print(f"Assignment {assignment_id} has been submitted.")
    else:
        print(f"Assignment {assignment_id} not found or not in the 'DRAFT' state.")

# Call the function with the assignment id
submit_assignment(4)

print("Sucessfully created fake users")
