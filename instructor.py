class instructor:
    def __init__(self):
        self.__instructor_name=None
        self.__experience=None
        self.__avg_feedback=None
        self.__technology_skills=None

    
    def get_instructor_name(self):
        return self.__instructor_name
    def get_experience(self):
        return self.__experience
    def get_avg_feedback(self):
        return self.__avg_feedback
    def get_eligibility(self):
        if self.__experience>3 and self.__avg_feedback>=4.5:
            return True
        if self.__experience<=3 and self.__avg_feedback>=4:
            return True
        else:
            return False
    
    def allocate_course(self,technology):
        if (technology==self.set_technology_skill) or ((technology=="c++")):
            return True
        else:
            return False


