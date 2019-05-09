# CS3398-Vulcan-S2019

## [UPair] (working title)

### Our Vision:

Our team of four will create an application targeted at the students of universities in an attempt to facilitate the creation of study groups. The application will help students who share similar schedules collaborate and study more efficiently.
  
### Welcome to UPair!

UPair is an application that allows students to pair up with other students that share overlapping class schedules in order to facilitate grouping up to study. This should allow students to be more successful in their scholastic career. This application is unique in its ability to facilitate interconnectivity between students both on and off campus.

### Help Support Development! 

UPair can expand and spread to many different universities across the globe with help in the form of: server access at participating universities, a dedicated website, and an expanded development team to maintain and push out updates.

### Current State of Program (As of end of Sprint 2)

UPair is currently non functional as the code is still be created by the development team. The development team is currently making progress toward runnable code. Current steps that are being taken are: further development of program backbone, creation of database operation code, creation of program flow, and design of a graphical user interface. The website is nearly complete but requires additional backend code to function properly. The backend is set up and functions but is incomplete. The database is fully functional.
***
**REVIEW**
FEATURE AND ACCOMPLISHEMTS PER TEAM MEMBER:
-Example of artifact or code. reference to your personal readme. What your commits are. Status of the project and each of our next steps.

### •	 **Jacob Gotcher**,  
Sprint 1: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/README.txt
Front side and driver file app.py for the web application folder.  
  
Sprint 2: (identify artificants from sprint 2 and link, add a what's next) 
https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/static/main.css
Made changes to front-side webpages. Modified aspects of the CSS to have a cleaner looking page. 
  
My largest responsibility coming into Sprint 3 is to have all the front-side code uploaded to GitHub. Also, the importance of the group getting together cannot be overstated. I will take the responsibility for putting the disparate aspects of the project together. 

Retrospective:
We have continued to communicate well on Slack, but we should be meeting in person much more often.
Our schedules are impeding our group from doing better as it prohibits us from meeting in-person.
To improve, if we can meet on the weekends one time during our next Sprint for 3 hours, we could accomplish much.

Sprint 3: I made changes to the about page and took of an artifact from a prior version. 
https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/templates/about.html

  


### • 	**Jon-Paul Kasper**,  
Sprint 1: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/tree/master/python%20backbone  
These files are notes used for creation of the Python backend. The code and notes are used to modify the operation of the program as it is developed. The User Class python file is to be used for the creation of different user objects. The Classes Class python file is to be used for the creation of different class objects. The Group Class python file is to be used for the creation of different group objects. All of these files will be modified as the program is developed to adapt to the needs of the program.

_WHAT'S NEXT_
Determine what needs to be built next in the back end. Build what is required for the back end. Work with Jacob and Peter to connect the back end with the database and website. Determine if there are any extras that can be built for the project.
  
Sprint 2: (identify artificants from sprint 2 and link, add a what's next)  
Created a work in progress UPair logo using input from other team members. Logo was uploaded but doesn't exist on git for some reason and file has been removed from personal PC.
  
_WHAT'S NEXT_  
Recreate the logo and re-upload for future sprint. Follow up with Sprint 1 for "What's Next".

Sprint 3: UPair Logo: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/UPair_logo_1.png
          UPair Tutorial Script: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/User%20Tutorial%20Script.txt
Created and completed the UPair logo to be used as part of the face of the application. Created a basic written script to be used for the english section of the code that makes up the tutorial. 
  
### •	**Cameron Valdez**,  
Sprint 1: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/DatabaseCalls.py  


Back-end work in python for the driver file instantiating the database. All queries for data within the database will be held here.
_STATUS_ 
Working on translating commented SQL query into a Python statement. Writing additional python statements to pull student information.
_WHAT'S NEXT_
After this is done, I will move on to working on a match method that will provide a list of user's emails to mass contact. 

Sprint 2: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/DatabaseCalls.py
          Additional functions pulled into DataBasecalls.py. Peter and I figured out the correct syntax to use when querying        the SQL database. Continued to develop functions to operate as the functionality of the website.
          Also, I fixed a cache issue we were having with Flask. Although we were making changes to the website html and css files, no changes were being refelected locally. Clearing the cache, hard killing the respective process, and restarting Flask seemed to do the trick. This is a little known issue with Flask that can occur depending on the FLASK_ENV variable used in the configuration. What we have uploaded onto the remote repository should now work on each of our computers assuming you have the correct dependencies.
 
_STATUS_  
The database needs to be connected with the website. A user is not able to access their information in the database yet, but the UI of the website is set up.
  
_WHAT'S NEXT_  
The written database functions will be called in the main app.py file and a tutorial will be fully fleshed out to walk users through the process.

Sprint 3: https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/emailsvc.py
          https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/static/popupstyle.css
          https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/templates/pair.html
          https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/app.py

During Sprint 3, I set up the automated emailing service, made the website sessionable for different users, and provided a pop-up tutorial when a user logs in.

_STATUS_ 
Emailing, sessions, and the tutorial is finished.
_WHAT'S NEXT_
Refining the tutorial (how it looks, etc) and making logout/login disappear upon login.


### •	**Peter Cowsar**, 

Artifacts:  
Sprint 1: [Database](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/UPair.bak), [Database fill data](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/UPair_fill_data.sql), [Image displaying table structure](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/UPair_Table_Structure.png)  
&nbsp;&nbsp;&nbsp;&nbsp;*Database: This is a backup file for the database that can be used to recreate the database structure and contents. It is not possible to upload an immediately runnable database.  
&nbsp;&nbsp;&nbsp;&nbsp;*Database fill data: Some of the insert statements that were used to fill the table with mock data.  
&nbsp;&nbsp;&nbsp;&nbsp;*Table structure: Shows the structure of the tables in the database.  
&nbsp;&nbsp;&nbsp;&nbsp;What's next: Work with Jon and Jacob to connect the database to the python backend and website. Add more mock data. Possible modifications to database if necessary.  
  
Sprint 2: [Darkmode css](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/darkmode.css) This is the css for applying darkmode to the website. It adjusts the color of multiple elements to make it easier on the eyes, [Updated DatabaseCalls.py](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/DatabaseCalls.py) This change allows the backend to pull in a pre-structured message from the database that the code can than format into a message relevant to particular users.  
  
Spring 3: [Database calls update](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/DatabaseCalls.py) This update allowed pulling user emails from shared classes. [Main app update](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/app.py) This update allowed running the code that sent emails out to potential partners. [Database update](https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/UPair.bak) This update included some changes and additions that allowed the email code to function properly.  
  
_STATUS_  
The program is functional but needs polishing. Some additional features would improve the app.
_WHAT'S NEXT_  
If the app were to be continued the next step would be allowing students to sign up for their own schedules when it is not possible to get the data from the University.  
  
***
## **SPRINT 1 RETROSPECTIVE**  
### _WHAT WENT WELL AND WHAT DIDN'T_  
•	Everyone was willing to work and did what they could.  
•	Everyone understood and accepted their role.  
•	Everyone communicated when needed; everyone was responsive.  
•	The team could have benefited from meeting in person more often.    
•	The team struggled to produce initially due to a learning curve.  
•	**Peter Cowsar**:  
&nbsp;&nbsp; I got the database to a functional stage that could be used to test and create the application.  
&nbsp;&nbsp; I could have helped initiate the process of joining the database with the other application components.  
•	**Jacob Gotcher**: Made changes to front-side webpages. Modified aspects of the CSS to have a cleaner looking page. 
•	**Jon-Paul Kasper**: Classes for the backend using python  

•	**Cameron Valdez**: Python backend working to integrate the database.
  

### _WHAT MIGHT BE IMPEDING US FROM PERFORMING BETTER_  
•	The team's various schedules are not very compatible. Multiple meet ups are necessary to meet with every group member.

### _WHAT CAN WE DO TO IMPROVE_  
•	The team can improve by meeting more often and developing a better understanding of the other members' work.  
•	**Peter Cowsar**: I could improve by scheduling times to meet with individual group members and scheduling my own working time. This would increase the quality and efficiency of my working hours significantly.  

•	 **Jacob Gotcher**: I need to work on the UI/UX of the front side website to make the site user friendly and aestheticly pleasing . I really need to communicate better with my teammates about the progress of all assignments and projects. 

•**Jon-Paul Kasper**: Be able to meet up with teammates at least one a week	  

•**Cameron Valdez**: I fixed a cache issue we were having with Flask.

## **SPRINT 2 RETROSPECTIVE**  
### _WHAT WENT WELL AND WHAT DIDN'T_  
•Everyone was on the same page as far as what was needed.  
•	All team members helped come to agreement on the Sprint Issues and decide a direction.  
•	The team communicated well on Slack for every assignment.
•	Compared to last sprint, a few individuals from the team met up to make crucial decisions.  
•	While we were able to meet in person, we need to try and all meet at least once (with every group member present) to get on the same page. 
  
•	**Peter Cowsar**: I coded the backend to pull in a pre-structured message from the database that the code can than format into a message relevant to particular users.  
•	**Jacob Gotcher**: I built the front side website and coded the initial app.py driver file.  
•	**Jon-Paul Kasper**: Made the logo.  
•	**Cameron Valdez**: Python backend working to integrate the database and fixed our issue with Flask.
  

### _WHAT MIGHT BE IMPEDING US FROM PERFORMING BETTER_  
•	The team's various schedules are not very compatible. Multiple meet ups are necessary to meet with every group member and even then it is difficult.

### _WHAT CAN WE DO TO IMPROVE_  
•	The team can improve by meeting more often and developing a better understanding of the other members' work.  
•	**Peter Cowsar**: I could improve by scheduling times to meet with individual group members and explaining my work. I could make sure to meet with at least one member per week.  
•	**Jacob Gotcher**: I need to manage my workflow better and update the Sprint, GitHub, and other teammates. I can ensure my workflow improves by scheduling hours and notifying my teammates when I do get work done and when I know I will be unable to get work done.  
• **Jon-Paul Kasper**: Be able to meet up with teammates at least one a week	  
• **Cameron Valdez**: Meeting with each team member individually and get what I need from them (since our schedules don't mesh well together). To do this I can ask specific people their availability as soon as the need arises.  

## **SPRINT 3 RETROSPECTIVE**
### _WHAT WENT WELL AND WHAT DIDN'T_

**Jon-Paul Kasper**: Logo was completed and finalized. Written script for the application tutorial was completed.  
**Jacob Gotcher**:I changed the about page and removed the sidebar that was an artifact from an earlier version. It was difficult to get through the Sprint becasue of a challenging class schedule and year-end course work. I think we all tried to fulfill our individual mandates, but may have come up short of our group expectations. Some of my work this Sprint
https://github.com/cs3398-vulcans-ponfarr/UPair-TxState-Project/blob/master/se_app/templates/about.html  
**Peter Cowsar**: I did well early in our sprint but did not get much done towards the middle of the sprint because I became too busy with other classes. That being said; at the end of the sprint I was able to make a lot of progress that helped the app get into a functional state.  
**Cameron Valdez**:  During Sprint 3, I set up the automated emailing service, made the website sessionable for different users, and provided a pop-up tutorial when a user logs in. All of these things ended up being finished in the end, so that went well enough. Towards the beginning of the sprint, however, I had to work a lot so I was off to a late start.

  
### _WHAT MIGHT BE IMPEDING US FROM PERFORMING BETTER_  
**Jon-Paul Kasper**:  
**Jacob Gotcher**: Overall, I think we needed to meet up more often as a whole group, but we got a lot completed.  
**Peter Cowsar**: I prioritized other classes above this one because I had more time to complete my work in this class.    
**Cameron Valdez**:  We did better than either of the other sprints: we met up more, and communicated better. But we still struggled to get a few of the project's functions done in a timely fashion.
  
### _WHAT CAN WE DO TO IMPROVE?_  
**Jon-Paul Kasper**:  
**Jacob Gotcher**:  Going forward, communicating with each other is of the upmost importance for group work in the future. It is the key to everything. Also, time management. Get it done early so you are not working furiously at the end.
**Peter Cowsar**: I could have improved by scheduling my time better so that I could get the work done over time instead of in quick bursts.  
**Cameron Valdez**: Going forward, I think that I could communicate what I'm working on, and what files I'm working on so that we don't have issues overwriting each other (this happened only a few times).
