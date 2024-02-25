class Applicant:
    __application_dict={"A":0,"B:0,"C:0}
    __applicant_id_count=1000
    
    def _init_(self,applicant_name):
        self.__applicant_name=applicant_name
        self.__applicant_id=None
        self.__job_band=None
        
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1
        self._applicant_id=Applicant._applicant_id_count
        
    def apply_for_job(self,job_band):
        if Applicant.__application_dict[job_band]==5:
            return -1
        else:
            Applicant.__application_dict[job_band]+=1
            self.generate_applicant_id()
            self.__job_band=job_band
            
    @staticmethod
    def get_application_dict():
        return Applicant.get_application_dict()
    def get_application_id(self):
        return self.__applicant_id
    def get_applicant_name(self):
        return self.__applicant_name