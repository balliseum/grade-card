# grade-card

## Endpoints

### /pupils/
- U can retrieve a list with all pupils (with extra filters);
- U can get info about each pupil by ID;
- U can create a new pupil;
- U can edit info about pupil;
- U can delete pupil;
- U can retrieve a list of grades for a specific pupil;
<br>

### /subjects/
- U can retrieve a list with all subject;
- U can get info about each subject by ID;
- U can create a new subject;
- U can edit info about subject;
- U can delete subject;
<br>

### /groups/
- U can retrieve a list with all groups;
- U can get info about each groups by ID;
- U can create a new groups;
- U can edit info about groups;
- U can delete groups;
<br>

### /grades/
- U can retrieve a list with grades;
- U can get info about each grade by ID;
- U can assign a new grade;
- U can edit grade;
- U can delete grade;

## Entities

class Pupil:
- id,
- first_name: str,
- last_name: str,
- group: Group
  
class Grade:
- id,
- grade: int,
- subject: Subject,
- pupil: Pupil

class Subject:
- id,
- name

class Group:
- id,
- name: str,
- pupils: backref

## Future Features
Teacher will be added!
