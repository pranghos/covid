import os
import validators
import ibm_db
import ibm_db_dbi

def main(args):
    ibm_db_conn = ibm_db.connect("DATABASE="+"BLUDB"+";HOSTNAME="+"dashdb-txn-sbox-yp-dal09-11.services.dal.bluemix.net"+";PORT="+"50000"+";PROTOCOL=TCPIP;UID="+"dnr61151"+";PWD="+"1l2mz7b+hclkfnj0"+";", "","")
    conn = ibm_db_dbi.Connection(ibm_db_conn)

    faqs = []    
    faqs = [('What is coronavirus?', 'Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS)'), ('Can you tell me about coronavirus?', 'Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS)'), ('Coronavirus', 'Coronaviruses are a large family of viruses that are known to cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS)')]

    print("\nPushing to Database...\n")  
    table_name = "COVIDFAQ"      
    for ques,ans in faqs:
        query = "INSERT INTO " + table_name + " VALUES('"+ques+"','"+ans+"')"
        stmt = ibm_db.exec_immediate(ibm_db_conn, query)
    print("Data Ingested to", table_name)
    
    return({"message": "success"})
    
    
if __name__ == "__main__":
    main({"input": "hi"})  