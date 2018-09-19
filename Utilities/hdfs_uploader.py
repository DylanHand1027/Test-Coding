import commands as com

print (' ')
print ('### Hadoop Quick Uploader ###')
print (' ')
filePath = raw_input('type the filepath of the file or directory you would like to upload: ')
print (' ')
fileName = raw_input('What would you like to name the file on Hadoop? ')
print (' ')
print com.getoutput('hdfs dfs -put ' + filePath + ' ' + fileName)
print ('Upload complete!')
print (' ')