queryStr = """
{
result: acClassificationPage {
  	id
  	student {
    	id
    	email
    	fullname
    	name
    	surname
  	}
  	semester {
    	id
    	subject {
      	id
      	name
      	program {
        	id
        	name
      	}
    	}
  	}
  	level {
    	id
    	name
  	}
  }

}

"""

mappers = {
    "id": "id",
    "studentid": "student.id",
    "studentemail": "student.email",
    "studentfullname": "student.fullname",
    "studentname": "student.name",
    "studentsurname": "student.surname",
    "semesterid": "semester.id",
    "subjectid": "semester.subject.id",
    "subjectname": "semester.subject.name",
    "programid": "semester.subject.program.id",
    "programname": "semester.subject.program.name",
    "levelid": "level.id",
    "levelname": "level.name",
}