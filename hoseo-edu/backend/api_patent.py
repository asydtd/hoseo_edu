# -*- coding: utf-8 -*-
print ("module [backend.api_patent] loaded")

from backend import app,manager
from backend_model.table_patent import *
from sqlalchemy import or_, and_,sql
from flask_restful import reqparse
from flask import make_response, jsonify, request, json, Response, send_from_directory
import requests
import re
import os
from datetime import datetime
db = DBManager.db
import json
from time import sleep
from datetime import datetime, timedelta

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import base64;

## 센싱케이트 장비에서 API를 통해 데이터를 송신
## JSON 데이터를 수신받아 AES 대칭 암호화 처리
## AES 암호화 데이터를 BASE64 인코딩 (DB에 평문으로 저장하기 위해)
## BASE64 인코딩 데이터 DB 추가
## 대칭키 패스워드 => p@ssw0rd

'''
    company: [
      {name:"허브테크", code : "10.8.0.10"},
      {name:"엘라이트", code : "10.8.0.14"},
      {name:"셋별", code : "10.8.0.30"},
      {name:"카오코리아", code : "10.8.0.26"},
      {name:"청호정밀", code : "10.8.0.22"}],
'''

@app.route('/api/v1/sensor_data_upload_edu', methods=['POST'])
def sensor_data_upload_edu_api():

    def sensor_encryption(inputed_data):
        #key생성,바이너리화
        print('inputed_data:',inputed_data['sensors_msg'])
        sensor_password = 'p@ssw0rd'
        sensor_password = sensor_password.encode('utf8')
        key = hashlib.pbkdf2_hmac(hash_name='sha256', password=sensor_password, salt=b'$3kj##agh_', iterations=100000)
        encrypt_text = str(inputed_data['sensors_msg']).encode('utf8')
        #패딩
        aes = AES.new(key, AES.MODE_ECB)
        Block_Size = 256
        padded_text = pad(encrypt_text, Block_Size)
        #암호화
        encrypted_text = aes.encrypt(padded_text)
        print("encrypted_text: ", encrypted_text)
        data = base64.b64encode(encrypted_text)
        return data

    def insert_sensor_data_source(input):
        new_msg = TB_SENSOR_UPLOAD()
        new_msg.sender_ip = input['sender_ip']  ## 창원 DB 서버 보내는곳 서버 IP
        new_msg.company_id = input['company_id'] ## 센싱게이트웨이 소속 회사 IP
        new_msg.sensors_msg = json.dumps(input['sensors_msg']) ## 센싱게이트에서 보네는 센서 데이터 JSON 리스트 형태
        new_msg.created_date = datetime.now()
        db.session.add(new_msg)
        obj = {
            "sender_ip": input['sender_ip'],
            "company_id": input['company_id'],
            "sensors_msg": input['sensors_msg'],
            "created_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        db.session.commit()

        return None

    def insert_sensor_data_encrypt(input):
        input['sensors_msg'] = sensor_encryption(input) ## 암호화 수행

        new_msg = TB_SENSOR_UPLOAD_ENCRYPT()
        new_msg.sender_ip = input['sender_ip']  ## 창원 DB 서버 보내는곳 서버 IP
        new_msg.company_id = input['company_id'] ## 센싱게이트웨이 소속 회사 IP
        new_msg.sensors_msg = input['sensors_msg'] ## 센싱게이트에서 보네는 센서 데이터 JSON 리스트 형태
        new_msg.created_date = datetime.now()
        #print("created_date")
        db.session.add(new_msg)
        obj = {
            "sender_ip": input['sender_ip'],
            "company_id": input['company_id'],
            "sensors_msg": input['sensors_msg'],
            "created_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        db.session.commit()

        return None


    print("sensor_data_upload")
    result = {
        "ACK":"SUCCESS",
        "MSG":""
    }
    parser = reqparse.RequestParser()
    parser.add_argument("data", type=str, location="json")
    data = parser.parse_args()
    print("data : ", data)
    data_body = data['data'].replace("'", "\"")
    input = json.loads(data_body)

    insert_sensor_data_source(input)
    insert_sensor_data_encrypt(input)

    return make_response(jsonify(result), 200)

## DB 암호화 되어 있는 메시지를 디코딩하여 리턴함
@app.route('/api/v1/sensor_data_descryption', methods=['GET'])
def sensor_data_descryption_api():
    data = TB_SENSOR_UPLOAD_ENCRYPT.query.all()

    sensor_password = 'p@ssw0rd'
    sensor_password = sensor_password.encode('utf8')
    key = hashlib.pbkdf2_hmac(hash_name='sha256', password=sensor_password, salt=b'$3kj##agh_', iterations=100000)
    aes = AES.new(key, AES.MODE_ECB)
    return_list = []
    for dataline in data:
        text = dataline.sensors_msg
        bs64Text = base64.b64decode(text)

        decrypted_text = aes.decrypt(bs64Text)
        Block_Size = 256
        unpadded_text = unpad(decrypted_text, Block_Size)
        print("unpadded_text: ", unpadded_text.decode('utf8'))
        return_list.append({
            'decoder_data': unpadded_text.decode('utf8')
        })

    result = {
        "data_list":return_list
    }
    return make_response(jsonify(result), 200)