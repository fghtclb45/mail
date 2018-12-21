import smtplib as smt
import sys

def help():
    print("[USAGE] --help")
    print("-sn & --sender     Gönderilen kişinin e-mail adresi")
    print("-s & --send   Gönderilecek kişinin e-mail adresi")
    print("-ps & --password  E-posta'nın şifresi")
    print("-r & --read    Gönderilecek mail adresinin içeriğini içeren txt dosyası")
try:
    if sys.argv[1] in ["-h","--help"]:
        help()
    elif sys.argv[1] in ["-sn","--sender"]:
        if sys.argv[3] in ["-s","--send"]:
            if sys.argv[5] in ["-ps","--password"]:
                if sys.argv[7] in ["-r","--read"]:
                    with open(sys.argv[8],"r+") as f:
                        data = f.read()
                    mail = smt.SMTP("smtp.gmail.com",587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login(sys.argv[2],sys.argv[6])
                    mail.sendmail(sys.argv[2],sys.argv[4],data)
                    
except IndexError:
    help()
except:
    print("Mail güvenlik ayarlarını kontrol ediniz.")
            
"""
except:
    print("Mail güvenlik ayarlarını kontrol ediniz...")
except IndexError:
    help()

"""
