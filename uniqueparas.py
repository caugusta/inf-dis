#Purpose: read in a file with the parameters of the neighbourhood epidemic, output a file that has only the unique settings.
#This was necessary because there was an error writing 'parameters_neighbourhood_Dec23.txt' file, and I needed to know
#which epidemics had to be re-run. They were re-run in '..._redo.txt', and I double-check that they were the correct parameters 
#by reading them in using this program. 

#http://stackoverflow.com/questions/1215208/how-might-i-remove-duplicate-lines-from-a-file
lines_seen = set() # holds lines already seen
outfile = open('uniqueparas.txt', "w")
for line in open('parameters_neighbourhood_Dec29.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
for line in open('parameters_neighbourhood_Dec29_redo.txt', 'r'):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
