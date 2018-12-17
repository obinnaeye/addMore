from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABcARzh0KDJhP35yjDMhmmZK4qbyZeFgV3E_ov1cwRtgtIIGdUqFG_ND4fq7vwzjrImBOFAw2WCL43nkhA0806f-CPZXbIftCZ3JRDtnx8pgIUJy3BWhdYSUZgk8f69ciQ6T2sOCUaVU4071F3wEgk5GDduRKGyvHH9w8ha9FrUS99vIvrlhj_suL93woRC-29wXPQH'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()

# https://engineering-application.britecore.com/e/t30e118s10t/ImplementationEngineer