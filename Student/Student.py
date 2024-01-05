class Student:

    def __init__(self, first_name, last_name, lessons=None, is_graduated=False):
        self.first_name = first_name
        self.last_name = last_name
        self.lessons = [] if lessons is None else lessons
        self.is_graduated = is_graduated

    def get_student_full_name(self):
        return self.first_name + " " + self.last_name
