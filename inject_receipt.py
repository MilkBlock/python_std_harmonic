import requests
import json
import threading

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def read_post_set(img_path):
    _app_id = '6b07d2d756f3be15198633de37dcc852'
    _secret_code = 'a38872198de6545a6464969c71ef1272'
    url = 'https://api.textin.com/robot/v1.0/api/receipt'
    head = {}
    try:
        image = get_file_content(img_path)
        head['x-ti-app-id'] = _app_id
        head['x-ti-secret-code'] = _secret_code
        result = requests.post(url, data=image, headers=head)
        set_record(result.json())
    except Exception as e:
        print(img_path," 请求失败并抛出异常")
        print(str(e))


def set_record(d):
    if(d["message"]!="success"):
        print("message :fail")
        return
    d= d["result"]
    print("bname",d["item_list"][3]["value"])
    print("bcategory","餐饮")
    print("note",d["item_list"][3]["value"])
    print("payment","支付宝")
    print("amount",d["item_list"][0]["value"])
    print("btime",d["item_list"][1]["value"])
    print("isreceipt",True)
    print(d)

if __name__ == "__main__":
    read_post_set(img_path=r"C:\Users\23869\Desktop\ticket_receipt_acg_3.jpg")