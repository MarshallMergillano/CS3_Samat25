class Patient:
  def __init__(self,name,bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount
  def get_name(self):
    return self.__name
  def set_name(self):
    self.__name = name
  def get_bill_amount(self):
    return self.__bill_amount
  def set_bill_amount(self,bill_amount):
    self.__bill_amount = bill_amount
  def display_info(self):
    print("Patient Name: ",self.__name)
    print("Original Bill:",self.__bill_amount)
  def calculate_bill(self):
    return self.__bill_amount

class PhilHealthPatient(Patient):
    def calculate_bill(self):
     return self.get_bill_amount() * 0.8

class SeniorPatient(Patient):
    def calculate_bill(self):
     return self.get_bill_amount() * 0.85

r_patient = Patient("Sam Aguilar",15000)
ph_patient = PhilHealthPatient("Ara Maglaya",15000)
s_patient = SeniorPatient("King Quiambao",15000)

print("Hospital Billing System")
print("-----------------------\n")

for patient in [r_patient, ph_patient, s_patient]:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: {patient.get_bill_amount():,.2f}")
    print(f"Final Bill: {patient.calculate_bill():,.2f}\n")
    
