class studentclass:
    def __init__(
        self,
        full_name="",
        date_of_birth="",
        age="",
        gender="",
        mobile_number="",
        email_address="",
        password="",
        preferred_language="",
        school_college_name="",
        class_grade="",
        board_curriculum="",
        academic_year="",
        subjects=None,
        current_level=None,
        areas_of_help=None,
        parent_name="",
        relationship_with_student="",
        parent_mobile_number="",
        parent_email_address="",
        preferred_communication_method="",
    ):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.password = password
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year
        self.subjects = subjects if subjects is not None else []
        self.current_level = current_level if current_level is not None else {}
        self.areas_of_help = areas_of_help if areas_of_help is not None else []

        self.parent_name = parent_name
        self.relationship_with_student = relationship_with_student
        self.parent_mobile_number = parent_mobile_number
        self.parent_email_address = parent_email_address
        self.preferred_communication_method = preferred_communication_method

    def setUserNameAndPassword(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def setPrimaryInformation(self, full_name, date_of_birth, age, mobile_number, preferred_language, school_college_name, class_grade, academic_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.mobile_number = mobile_number 
        if len(mobile_number) != 10 or not mobile_number.isdigit():
            raise ValueError("Mobile number must be a 10-digit number.")   
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.academic_year = academic_year 
