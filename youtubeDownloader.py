from pytube import YouTube
import os 

currentDir = os.getcwd()

# def checkDup(title):
# 	if not os.path.isdir(os.path.join(currentDir,'Music')):
# 		os.mkdir(os.path.join(currentDir,'Music'))

# 	allFiles = [file for file in os.listdir(os.path.join(currentDir,'Music')) if file.endswith('.mp3')]

# 	title = title+'.mp3'	

# 	print(title)
# 	print(allFiles)
# 	if title in allFiles:
# 		print('Already Downloaded')
# 		return False
# 	else:
# 		return True

def DownloadFile(url):
	try:
		yt = YouTube(url)

		dwnld = yt.streams.filter(type='audio').last().download()
		oldName, oth = os.path.splitext(dwnld)
		newName = oldName + '.mp3'
		if not os.path.isdir(os.path.join(currentDir,'Music')):
			os.mkdir(os.path.join(currentDir,'Music'))
		try:
			os.rename(dwnld, os.path.join(currentDir,'Music',os.path.basename(newName)))
			print('\nFile Downloaded')
		except:
			print('\nSomething went wrong')
	except:
		print('\nConnection Error')
	

if __name__ == "__main__":
	choice = 'a'
	while(choice=='a'):
		print('Enter Your Video Link to convert into mp3: ')
		url = input()

		DownloadFile(url)

		print('\nEnter "a" for again, eny key to exit: ')
		choice = input()
