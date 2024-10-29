from app.extension import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    user_password = db.Column(db.String(255), nullable=False)

    # 保护字段，比如xxx.password,直接报错
    @property
    def password(self):
        raise ArithmeticError("password是不可读字段")

    # 设置密码，加密，比如,xxx.password=xxxx
    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)


class Patient(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_name = db.Column(db.String(255), nullable=False, unique=True)
    patient_department = db.Column(db.String(255))
    patient_description = db.Column(db.String(255))
    patient_is_solved = db.Column(db.Boolean, default=False)
