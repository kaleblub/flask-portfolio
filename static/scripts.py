import os, sass

def getPostFiles(path):
	#############################
	# Get the list of post files
	#############################
	contentFolder = os.listdir(path)
	endFiles = {} # was list[] => now dict{}
	for yearFolder in contentFolder:
		if yearFolder[-4::] not in endFiles:
			endFiles[yearFolder[-4::]] = []
		yearFolder = path + yearFolder
		#print(os.listdir(yearFolder))
		for file in os.listdir(yearFolder):
			endFiles[yearFolder[-4:]].append(file)
	return endFiles # Used to return a List/Now returns a Dict

def returnSeperatedData(file):
	postData = {}
	with open(file, 'r') as f:
		postData['content'] = []
		for line in f.readlines():
			if 'title:' in line:
				postData['title'] = line.split(': ')[1]
			elif 'author:' in line:
				postData['author'] = line.split(': ')[1]
			elif 'date_created:' in line:
				postData['date_created'] = line.split(': ')[1].rstrip().split('-')#To translate month numbers into the names => toDateFormat(line.split(': ')[1])
			elif 'summary:' in line:
				postData['summary'] = line.split(': ')[1]
			elif 'tags:' in line:
				postData['tags'] = line.split(': ')[1]
			elif '---' not in line:
				postData['content'].append(line)
	return postData # Dict


def getPostInfo(postFileContent):
	#####################################################################################
	# Read The Post File & Seperate Each Piece Of Information, Returning Each Seperately
	#####################################################################################
	'''
	Get the data within the 
	---
	title
	summary
	etc
	---
	'''
	for line in postFileContent:
		if line == "---":
			return 0# title, author, date_created, summary, tags, content


class DatabaseInteractions():
	##########################################
	# Class With All Useable Database Actions
	##########################################
	def __init__(self, session):
		self.session = session

def checkDatabaseForTags(session, list_of_tags):
	#########################################################
	#	1. Using the list of the given tags from each post,
	#	2. Check each tag with the tags within the database
	#	3. If it is already saved in the database,
	#	4. Just add and commit to session
	#########################################################
	return 0


def addTagidPostidToRelationshipTable(session, tagId, postId):
	##################################################################
	#	1. Add the tag and post relationship to the Association table
	##################################################################
	session.add(AssociationTable(tagId=tagId, postId=postId))
	return session


def addTagToDatabase(session, tagName, postName):
	####################################################
	#	1. Use the database session,
	#	2. Add the tag to the session and commit it
	#	3. Add tagId & postId to the association table
	####################################################
	postId = session.query(Post).filter_by(title=postName).id
	session.add(Tag(title=tagName))
	return 0


def compile_sass_to_css(sass_map):
    for source, dest in sass_map.items():
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))
        print(f"{source} ==== COMPILED TO ==== {dest}")


def toDateFormat(date):
	#####################################################
	# Transforms Date From utcnow() to 'Month <int:day>'
	#####################################################
	date = date.split('-')
	year, month, day = date[0], date[1], date[2].strip('\n')
	if month == '1':
		month = 'January'
	elif month == '2':
		month = 'February'
	elif month == '3':
		month = 'March'
	elif month == '4':
		month = 'April'
	elif month == '5':
		month = 'May'
	elif month == '6':
		month = 'June'
	elif month == '7':
		month = 'July'
	elif month == '8':
		month = 'August'
	elif month == '9':
		month = 'September'
	elif month == '10':
		month = 'October'
	elif month == '11':	
		month = 'November'
	elif month == '12':
		month = 'December'
	return (day, month, year)


def getWordCount(postContent):
		contentWordList = content.split(" ")
		wordCount = 0
		for word in content:
			wordCount += 1
		return wordCount


def calcReadingTime(word_count):
	##############################################
	# Calculates Total Reading Time For Blog Post
	##############################################
	time = str(word_count / 200).split('.') # Divide the word_count by 200 for words per minute
	minutes = int(time[0])
	seconds = float('0.' + time[1]) * 0.6
	if seconds >= 0.3:
		minutes += 1
	# print(f"Takes {minutes} minutes to read")

calcReadingTime(783)
calcReadingTime(500)
calcReadingTime(1000)