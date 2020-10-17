FROM python:3.6.7
RUN pip install flask flask_restful flask_cors flask_jwt_simple waitress pandas
RUN pip install xlsxwriter xlrd joblib requests
RUN python -m pip install pymongo
RUN pip install cloudpickle
RUN mkdir /app
WORKDIR /app/
COPY . /app/
