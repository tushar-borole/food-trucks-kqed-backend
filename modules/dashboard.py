#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from modules.model import conn



class Dashboard(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self):
        """api to retrive details of the patient by it id"""

        patient = conn.execute("SELECT * FROM foodtruck").fetchall()
        return patient

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        pat_first_name = patientInput['pat_first_name']
        pat_last_name = patientInput['pat_last_name']
        pat_insurance_no = patientInput['pat_insurance_no']
        pat_ph_no = patientInput['pat_ph_no']
        pat_address = patientInput['pat_address']
        conn.execute("UPDATE patient SET pat_first_name=?,pat_last_name=?,pat_insurance_no=?,pat_ph_no=?,pat_address=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name, pat_insurance_no,pat_ph_no,pat_address,id))
        conn.commit()
        return patientInput