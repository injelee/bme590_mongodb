from pymodm import connect
from pymodm import MongoModel, fields
from flask import Flask, request

connect("mongodb://vcm-1848.vm.duke.edu/bme590_mongodb")


class get_patient_info(MongoModel):
    name = fields.CharField()
    age = fields.CharField()
    bmi = fields.CharField()

app = Flask(__name__)


@app.route("/api/new_patient", methods=['POST'])
def new_patient():
    data = request.json
    patient = get_patient_info(data.name, data.age, data.bmi)
    patient.save()
    print(patient.name)


@app.route("/api/average_bmi/<string:age>", methods=['GET'])
def average_bmi(age):
    avg_bmi = []
    for patients in get_patient_info.objects.raw({'age': age}):
        avg_bmi.append(float(patients.bmi))
    return avg_bmi.mean()






