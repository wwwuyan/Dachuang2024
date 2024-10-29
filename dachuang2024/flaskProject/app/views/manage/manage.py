from flask import request
from flask.views import MethodView

from app.extension import db
from app.models import Patient


class ManageApi(MethodView):

    def get(self, patient_id):
        if not patient_id:
            patients = Patient.query.all()  # 从数据库中获取所有患者数据
            patient_list = [{'id': patient.id, 'name': patient.patient_name, 'department': patient.patient_department,
                             'description': patient.patient_description, 'is_solved': patient.patient_is_solved} for patient in
                            patients]  # 将每个患者的数据转换为字典形式
            return {
                'status': 'success',
                'data': patient_list  # 将患者列表添加到返回结果中
            }
        patient: Patient = Patient.query.get(patient_id)
        if patient is None:
            return {
                'status': 'error',
                'message': '未找到指定患者',
            }
        patient_list = [{'id': patient.id, 'name': patient.patient_name, 'department': patient.patient_department,
                         'description': patient.patient_description, 'is_solved': patient.patient_is_solved}]
        return {
            'status': 'success',
            'data': patient_list  # 将患者列表添加到返回结果中
            }

    def post(self):
        pass

    def put(self, patient_id):
        patient = Patient.query.get(patient_id)
        patient.patient_description = request.form.get('description')
        patient.patient_is_solved = True
        db.session.commit()
        return {
            'status': 'success',
            'message': '数据修改成功'
        }

    def delete(self, patient_id):
        pass


manage_view = ManageApi.as_view('manage_api')
