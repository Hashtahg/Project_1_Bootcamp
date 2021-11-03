import csv
from pathlib import Path

#def writeToCSV(csvSavePath,dictionary1, dictionary2):
def writeToCSV(fileName1, fileName2,dataframe1, dataframe2):
#def writeToCSV(fileName1, dataframe1): for Chaim if he wants to combine it

    #header = ["Lender","Max Loan Amount", "Max LTV,Max DTI", "Min Credit Score", "Interest Rate"]

    #print(qualifying_loans) #Just checking variable value
    #print(csvSavePath) #Just checking variable value
    #csvpath = Path(csvSavePath)
    #with open(csvpath, 'w', newline='') as csvfile:
     #   csvwriter = csv.writer(csvfile)
    
    # Write our header row first!
        #csvwriter.writerow(header)
        #Write the rest of the csv by populating with qualifying loans. Thank you google for the syntax
        #https://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file

        #wr = csv.writer(csvfile)
        #wr.writerows(dictionary1)
        #wr.writerows(dictionary2)
       
       # for row in qualifying_loans:
       #     csvwriter.writerow(row.values())
      
        #created csv with dataframe1
        dataframe1.to_csv(fileName1, index=False)
        
        # created csv file with dataframe2
        dataframe2.to_csv(fileName2, index=False)
        
        print("Reports have been saved. Have a nice day!")



