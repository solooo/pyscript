
import qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data('''开票资料
公司名称：江苏华通晟云科技有限公司
统一社会信用代码：91320594MA1MBC5030
开户行：浙商银行股份有限公司苏州分行
银行帐号：3050020010120100106643
地址：苏州工业园区星湖街328号创意产业园2-B803室
电话：0512-62966662
''')
qr.make()

img = qr.make_image()

img.save("E:\\bill.png")