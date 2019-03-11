import csv

with open('/home/uvionics/data/Latest_mar6/shoppe/shopee_milkformula_SG_2019-01-01.csv') as fin:    
    csvin = csv.DictReader(fin)
 
   
    # Category -> open file lookup
    outputs = {}
    for row in csvin:
        cat = row[' SKU']
        # Open a new file and write the header
        if cat not in outputs:
         fout=open('/home/uvionics/data/Latest_mar6/shoppe_result/{}.csv'.format(cat), 'w') 
         dw = csv.DictWriter(fout, fieldnames=csvin.fieldnames)
         dw.writeheader()
         outputs[cat] = fout, dw
         
        # Always write the row
        outputs[cat][1].writerow(row)
        
    # Close all the files
    for fout, _ in outputs.values():
        fout.close()
        
