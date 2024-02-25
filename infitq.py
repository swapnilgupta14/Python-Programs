class Applicant:
    __application_dict = {'A': 0, 'B': 0, 'C': 0}
    __applicant_id_count = 1000
    def __init__(self, applicant_name):
        self.__applicant_id = None
        self.__applicant_name = applicant_name
        self.__job_band = None
    def generate_applicant_id(self):
        Applicant.__applicant_id_count += 1
        self.__applicant_id = Applicant.__applicant_id_count
    def apply_for_job(self, job_band):
        appli_list = Applicant
        if Applicant.get_application_dict()[job_band] >= 5:
            return -1
        else:
            Applicant.get_application_dict()[job_band] += 1
            self.generate_applicant_id()
            self.__job_band = job_band
 @staticmethod
    def get_application_dict():
        return Applicant.__application_dict

    def get_applicant_id(self):
 return self.__applicant_id
 def get_applicant_name(self):
 return self.__applicant_name
 def get_job_band(self):
 return self.__job_band
def main():
 n = int(input("Enter no. of applicants: "))
 for i in range(0, n):
 print("Applicant ", i + 1)
 applicant_obj = Applicant(input("Enter Applicant Name : "))
 if applicant_obj.apply_for_job(input("Enter Job Band(A/B/C) : ")) == -1:
 print("Cant Apply for the band")
 else:
 print("Applicant ID : ", applicant_obj.get_applicant_id())
 print("Name : ", applicant_obj.get_applicant_name())
 print("Applied Job Band : ", applicant_obj.get_job_band())
main()