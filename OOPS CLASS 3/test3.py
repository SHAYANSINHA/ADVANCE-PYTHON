# MULTIPLE INHERITANCE
class bank :

    def transaction(self):
        print("total transaction value ")
    def account_opening(self):
        print("this will show your account open status")
    def deposite(self):
        print("this will show your deposited amount ")
    def test(self):
        print("this is a test method form blank class")

class HDFC_bank : # this two classes  are not connected to each other
    def hdfc_to_icici(self):
        print("this will show all the transaction happend to icici through hdfc")

    def test(self):
        print("this is a test method form  hdfc blank ")

class ineuron_bank :
    def account_status_icici(self):
        print("this account status in icici bank .")


class icici(HDFC_bank,bank,ineuron_bank) : # THIS TIME MILTIPLE CLASSES
    pass

i=icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()
i.test() # if there is conflict it give very first argument we pass, here pass hdfc as first argument
i.account_status_icici()