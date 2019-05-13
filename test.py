import os

from LearnSelenium.config.send_msg import send_msg

case_dir = os.path.join(os.getcwd(), "case")
print(case_dir)

# msg='库存预警监控提醒：你好！顺义分公司ONT库存低于预警下限，请核实！'
# msg='您好！，您有终端领用已超过15天，请登录APP查看放装，'
# send_msg('15110253297', msg)

#send_mail(new_report)
msg = '您好：本次测试共14个用例，包含集中预约、调度质检、工单查询、调度中心报表、终端管理系统、门户、权限、企宽。自动化测试结果为 run=13 errors=2 failures=0详情请查看邮件'
send_msg('15110253297',msg)









