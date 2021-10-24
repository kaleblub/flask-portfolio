

def getWordCount(postContent):
		contentWordList = content.split(" ")
		wordCount = 0
		for word in content:
			wordCount += 1
		return wordCount


def getPostInfo(postFileContent):
	'''
	Get the data within the 
	---
	title
	summary
	etc
	---
	'''


# Compiles All SASS Files Into One CSS File
import sass
def compile_sass_to_css(sass_map):
    for source, dest in sass_map.items():
        with open(dest, "w") as outfile:
            outfile.write(sass.compile(filename=source))
        print(f"{source} ==== COMPILED TO ==== {dest}")

# Calculates Total Reading Time For Blog Post
def calcReadingTime(word_count):
	time = str(word_count / 200).split('.') # Divide the word_count by 200 for words per minute
	minutes = int(time[0])
	seconds = float('0.' + time[1]) * 0.6
	# print(f"{minutes=}", f"{seconds=}")
	if seconds >= 0.3:
		minutes += 1
	print(f"Takes {minutes} to read")

calcReadingTime(783)
calcReadingTime(500)
calcReadingTime(1000)