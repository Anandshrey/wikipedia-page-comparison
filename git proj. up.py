import wikipedia as wp
import os
from pathlib import Path

def wikipage2file(wikipedia_pagetitle, output_filepath):
    # function to write page in text file

    #declare empty page list
    pageList = []
    #validate pagetitele to be searched is not blank
    if (wikipedia_pagetitle == '') or wikipedia_pagetitle.isspace():
        print("Error: Invalid search argument!")
    else:
        try:
            #position to output filepath
            os.chdir(Path(output_filepath))

            #search pagetitle and populate pagelist
            pageList = wp.search(wikipedia_pagetitle)

            #set page to first search result in list
            wikipage = wp.page(pageList[0])

            #get title and content of selected page
            wikipageTitle = wikipage.title
            wikipageContent = wikipage.content
    
            #construct file name from page title by removing spaces
            filename = wikipageTitle.replace(" ","") + ".txt"                 
         
            #open file for writing, write title and content
            file = open(filename,"w",encoding='utf-8')
            file.write(wikipageTitle + "\n\n" + wikipageContent)
            file.close()
            print("Output written to file " + filename)

            #handle exceptions
        except FileNotFoundError:
            print("Error: Cannot find file/directory!")
        except IOError:
            print("Error: An error occurred trying to write file!")
        except:
            print("Search failed!")        
    return
  

def similar(x,y):
    result = ''
    # function to get similarity between 2 pages
    
    def getWords(page):
        # function to get words on a page

        #define empty set
        setofWords = set()

        #convert text to lower case
        text = page.content
        text = text.strip().lower()

        #extract words and add to set
        words = text.split(" ")
        for word in words :
            if (word != '') and (word not in setofWords):
                setofWords.add(word)
        
        return setofWords

    #get set words in page x and y
    xwords = getWords(x)
    ywords = getWords(y)

    #create set of words common in x and y
    xANDywords = xwords.intersection(ywords)
    #create set of words either in x or y
    xORywords = xwords.union(ywords)

    if len(xORywords) != 0:
        #calculate similarity
        result = round(len(xANDywords)/len(xORywords),4)
    return result
inp1=input("Enter the first page name")
inp2=input("Enter the second page name")

x = wp.page(wp.search(inp1)[0])
y = wp.page(wp.search(inp2)[0])
wp.set_lang("en")
print("Similarity = ", (similar(x,y)))

print(wp.page("python").images[0])
print(wp.page("java").images[0])
wikipage2file("Python", "C:\Shreyas")
query=input("Please Enter Your Query: ")
print("Response for your query-",wp.suggest(query))


