from pyrogram import Client , filters   #IMPORTING Client and filters from PYROGRAM PACKAGE : instatlled using pip3 install -U pyrogram
from dotenv import load_dotenv		#IMPORT dotenv package and load the contant from dotenv file locally here the file is hidden for securuity purpose and the api key's are uploaded in heroku config vars
import os				#IMPORT os Package to access the API KEY'S from .env locally and also to get them from heroku config vars 

load_dotenv()				#loading the variable from .env to current file

bot = Client(
		"my first project",
		api_id = os.getenv("API_ID"),				#get api_id from  https://my.telegram.org/apps
		api_hash = os.getenv("API_HASH"),			#get api_hash from  https://my.telegram.org/apps	
	 	bot_token = os.getenv("RNSITNOTESBOT_TOKEN")		#get bot_token from  https://my.telegram.org/apps

)
#start button--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('start') )  
def command1(bot, message):       
	    
	bot.send_message(message.chat.id, "I Can search through rnsit notes uploaded by @sanjaybyranna"),  
	bot.send_message(message.chat.id, "Follow this method :\nFor Ex: To search edmodule1 U have to serch it as \n/edmodule1"),
	bot.send_message(message.chat.id, "List of subjects the bot can give the notes are\n/mathsnotes\n/ntnotes\n/ednotes\n/dsdnotes\n/conotes\n/penotes\n/cpcnotes")
	
#list of subjects--------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('listofsubjects') )
def command(bot, message): 
	bot.send_message(message.chat.id, "List of subjects the bot can give the notes are\n/mathsnotes\n/ntnotes\n/ednotes\n/dsdnotes\n/conotes\n/penotes\n/cpcnotes")  

#maths list--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('mathsnotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/mathsmodule1\n/mathsmodule2\n/mathsmodule3\n/mathsmodule4\n/mathsmodule5"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


	#nt list--------------------------------------------------------------------------------------------------------------------------------------------------    
@bot.on_message(filters.command('ntnotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/ntmodule1\n/ntmodule2\n/ntmodule3\n/ntmodule4\n/ntmodule5")

	#ed list--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('ednotes') ) 
def command(bot, message):
	bot.send_message(message.chat.id, "/edmodule1\n/edmodule2\n/edmodule3\n/edmodule4\n/edmodule5")

	# dsd list--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('dsdnotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/dsdmodule1\n/dsdmodule2\n/dsdmodule3\n/dsdmodule4\n/dsdmodule5")

	#co list--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('conotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/comodule1\n/comodule2\n/comodule3\n/comodule4\n/comodule5")

	#pe list--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('penotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/pemodule1\n/pemodule2\n/pemodule3\n/pemodule4\n/pemodule5")

	#cpc list--------------------------------------------------------------------------------------------------------------------------------------------------    
@bot.on_message(filters.command('cpcnotes') ) 
def command(bot, message):       
	bot.send_message(message.chat.id, "/cpcmodule1\n/cpcmodule2\n/cpcmodule3\n/cpcmodule4\n/cpcmodule5")
	    

#links of notes are uploaded from here--------------------------------------------------------------------------------------------------------------------------------------------------


#ed notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('edmodule1') )
def command(bot, message): 
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/37"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/38"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('edmodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/91"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/39"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('edmodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/129"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('edmodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/128"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('edmodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/124"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/80"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 



#dsd notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('dsdmodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/44"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('dsdmodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/92"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/90"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('dsdmodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/103"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('dsdmodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/113"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/114"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('dsdmodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/143"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


#nt notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('ntmodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/136"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/43"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/35"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('ntmodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/137"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/84"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('ntmodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/138"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/121"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/83"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('ntmodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/134"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


@bot.on_message(filters.command('ntmodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/150"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/149"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/148"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/135"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/118"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/117"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/105"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 


#maths notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('mathsmodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "Sorry Not Found."),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('mathsmodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/151"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/152"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('mathsmodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/115"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('mathsmodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "Sorry Not Found."),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects")

@bot.on_message(filters.command('mathsmodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "Sorry Not Found."),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

#co notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('comodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/73"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/41"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('comodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/86"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/74"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/42"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('comodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/85"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/75"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('comodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/125"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/76"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects")

@bot.on_message(filters.command('comodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/126"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/77"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

#pe notes--------------------------------------------------------------------------------------------------------------------------------------------------
@bot.on_message(filters.command('pemodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/89"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/48"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/46"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('pemodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/87"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/49"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('pemodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/88?single"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('pemodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/140"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/104"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects")

@bot.on_message(filters.command('pemodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/116"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/111"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/109"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

#cpc notes
@bot.on_message(filters.command('cpcmodule1') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/34"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/65"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/71"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('cpcmodule2') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/34"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('cpcmodule3') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/34"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

@bot.on_message(filters.command('cpcmodule4') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/34"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/144"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects")

@bot.on_message(filters.command('cpcmodule5') )
def command(bot , message):
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/34"),
	bot.send_message(message.chat.id, "https://t.me/ECE3rdSemRnsitNotes2021/146"),
	bot.send_message(message.chat.id, "What to search notes again?\nThen click Here\n/listofsubjects") 

#end of uploades--------------------------------------------------------------------------------------------------------------------------------------------------
print("i am alive")




bot.run()
