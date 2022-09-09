import csv

infile = open('steps.csv','r')

csvfile = csv.reader(infile,delimiter=',')
write1 = open('avg_steps.csv','w')
csvfile2 = csv.writer(write1,delimiter=',')
jancount=0
febcount=0
marcount=0
aprcount=0
maycount=0
junecount=0
julycount=0
augcount=0
sepcount=0
octcount=0
novcount=0
deccount=0
numcount=0
jandenom=0
febdenom=0
mardenom=0
aprdenom=0
maydenom=0
jundenom=0
juldenom=0
augdenom=0
sepdenom=0
octdenom=0
novdenom=0
decdenom=0

write1.write('Month, Average Steps' + '\n')

next(csvfile)

for record in csvfile:
    if int(record[0]) is 1:
        jancount=jancount+1
        jandenom=jandenom+int(record[1])

    else:
        if int(record[0]) is 2:
            febcount=febcount+1
            febdenom=febdenom+int(record[1])

        else:
            if int(record[0]) is 3:
                marcount=marcount+1
                mardenom=mardenom+int(record[1])

            else:
                if int(record[0]) is 4:
                    aprcount=aprcount+1
                    aprdenom=aprdenom+int(record[1])

                else:
                    if int(record[0]) is 5:
                        maycount=maycount+1
                        maydenom=maydenom+int(record[1])

                    else:
                        if int(record[0]) is 6:
                            junecount=junecount+1
                            jundenom=jundenom+int(record[1])
                        
                        else:
                            if int(record[0]) is 7:
                                julycount=julycount+1
                                juldenom=juldenom+int(record[1])

                            else:
                                if int(record[0]) is 8:
                                    augcount=augcount+1
                                    augdenom=augdenom+int(record[1])

                                else:
                                    if int(record[0]) is 9:
                                        sepcount=sepcount+1
                                        sepdenom=sepdenom+int(record[1])

                                    else:
                                        if int(record[0]) is 10:
                                            octcount=octcount+1
                                            octdenom=octdenom+int(record[1])

                                        else:
                                            if int(record[0]) is 11:
                                                novcount=novcount+1
                                                novdenom=novdenom+int(record[1])

                                            else:
                                                if int(record[0]) is 12:
                                                  deccount=deccount+1
                                                  decdenom=decdenom+int(record[1])

write1.write('January: ' + str(round((jandenom/jancount),2))+'\n')
write1.write('February: ' + str(round((febdenom/febcount),2))+'\n')
write1.write('March: ' + str(round((mardenom/marcount),2))+'\n')
write1.write('April: ' + str(round((aprdenom/aprcount),2))+'\n')
write1.write('May: ' + str(round((maydenom/maycount),2))+'\n')
write1.write('June: ' + str(round((jundenom/junecount),2))+'\n')
write1.write('July: ' + str(round((juldenom/julycount),2))+'\n')
write1.write('August: ' + str(round((augdenom/augcount),2))+'\n')
write1.write('September: ' + str(round((sepdenom/sepcount),2))+'\n')
write1.write('October: ' + str(round((octdenom/octcount),2))+'\n')
write1.write('November: ' + str(round((novdenom/novcount),2))+'\n')
write1.write('December: ' + str(round((decdenom/deccount),2))+'\n')

write1.close()
infile.close()


                                        
            
    
