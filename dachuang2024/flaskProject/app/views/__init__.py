from app.views.utils.file import file_view
from app.views.detection.detection import detection_view
from app.views.utils.image import image_view
from app.views.reduction.reduction import reduction_view
from app.views.classification.classification import classification_view
from app.views.manage.manage import manage_view
from flask import Blueprint

bp = Blueprint('api', __name__)

bp.add_url_rule('/file', view_func=file_view, methods=['POST'])
bp.add_url_rule('/detection', view_func=detection_view, methods=['POST'])
bp.add_url_rule('/reduction', view_func=reduction_view, methods=['POST'])
bp.add_url_rule('/classification', view_func=classification_view, methods=['POST'])
bp.add_url_rule('/image/<path:filename>', view_func=image_view, methods=['GET'])
bp.add_url_rule('/patient', defaults={'patient_id': None}, view_func=manage_view, methods=['GET'])
bp.add_url_rule('/patient', view_func=manage_view, methods=['POST'])
bp.add_url_rule('/patient/<int:patient_id>', view_func=manage_view, methods=['GET', 'PUT', 'DELETE'])
