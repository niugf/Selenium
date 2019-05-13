import suds.client

def send_msg(phone,msg):
    sendsmsUrl = "http://10.224.132.133:7500/smsIRMS/smsSend_proxy?wsdl"
    sendsmsUrl = "http://10.4.61.79:7500/smsIRMS/smsSend_proxy?wsdl"
    xml = "<sms username='rms' password='Rms,528'><head system='system' service='service'  priority='2' seqno='12345'/><mobile>"+phone+"</mobile><message>"+msg+"</message></sms>"
    client = suds.client.Client(sendsmsUrl)
    service = client.service
    result = service.sendSMS(xml)
    print(result)




