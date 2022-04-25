
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "  "   # From Address of the mail
password = "  "   # Password 
toaddr = "  "     # To Address of the mail



msg = MIMEMultipart()


msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ABUSEVT"


html="""
<html>
<head>
<title>ABUSE VirusTotal</title>
</head>
<body>
<h1>ABUSE VirusTotal</h1>
<h3>Collection of IOCs</h3>
<table border="5" cell padding="15" cell border="10">
<tr>
<th>Type</th><th>id</th><th>Result</th></tr>
<tr>
<td>Domain</td>
<td>mojobiden.com</td>
<td bgcolor="red">Malicious</td></tr>
<tr>
<td>Domain</td>
<td>paymenthacks.com</td>
<td bgcolor="red">Malicious</td></tr>
<tr>
<td>Url</td>
<td>http://paymenthacks.com/?</td>
<td bgcolor="red">Malicious</td><tr>
<tr>
<td>Url</td>
<td>http://survey-smiles.com/</td>
<td bgcolor="red">Malicious</td><tr>
<tr>
<td>Url</td>
<td>http://crl.identrust.com/DSTROOTCAX3CRL.crl</td>
<td  bgcolor="green"> Not Malicious</td><tr>



<tr>
<td>Hash</td>
<td>  b06e2455a9c7c9485b85e9bdcceb8078 </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>  4034B53B9860591FD988DA82FF6575F9 </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>  598c53bfef81e489375f09792e487f1a </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>  d0512f2063cbd79fb0f770817cc81ab3 </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>   3f9a28e8c057e7ea7ccf15a4db81f362</td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td> a55bc3368a10ca5a92c1c9ecae97ced9  </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>  ba375d0625001102fc1f2ccb6f582d91 </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>72ed32b0e8692c7caa25d61e1828cdb48c4fe361   </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>   a63304592f422656d7abcb086915f9e799ad4641</td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>  80a29bd2c349a8588edf42653ed739054f9a10f5 </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td> e324a2c8fae0d26b12f00ac859340f8d9945a9c1  </td><td bgcolor="red">Malicious</td><tr>
<tr>
<td>Hash</td>
<td>   10d6d3c957facf06098771bf409b9593eea58c75</td><td bgcolor="red">Malicious</td><tr>
</body>
</html>


"""

msg.attach(MIMEText(html, 'html'))

filename = "Virustotal Malicious result.csv"
attachment = open(filename, "rb")

p = MIMEBase('application', 'octet-stream')

p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(fromaddr,password)

text = msg.as_string()

server.send_message(msg)
print('Mail send.....')

server.quit()