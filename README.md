# Penalty Kicks

Penalty kicks is a back end game, based on algorithms.
You don´t need to be a brilliant soccerplayer to have a chance in this game, just luck!
You start up the game with writing your name, and take a chance to name yourself as a famous soccerplayer and get the illusion to win with penalty shoots.
You will be asked to read instructions or not, so you don´t always have to schroll down a lot of text if you dont need to.
You don´t have to be nervous to make a misstake or break someting, since you get an errormessage and a retry if you dont use a valid input.
When the game ends you get questioned if you want to restart or not.

My idea for this game comes out of my soccerplayers in family and wish to practice the algorithm that comes with python.
When you are going to shoot that penalty "on life or death" you have to make a strategy and lot of thinking.

## Contents

* Features [Features](#features)
* Design [Design](#design)
* Flowcharts [Flowcharts](#flowcharts)
* Example of errors [Example of errors](#example of errors)
* Test [Test](#test)
* Technologies [Technologies](#Technologies)
* Deployment [Deployment](#Deployment)
* Acknowledgement [Acknowledgement](#Acknowledgement)
* Credits [Credits](#Credits)
  



## Features
When the game starts you have 6 directions to choose for the penalty: Left top or bottom, Middle top or bottom or Right Top or bottom.
They are shortened code, so it´s easy to text, but are explained so you dont get confused or have to remember the codes.
After your choice the computer makes a random choice which direction the goalkeeper will jump. If he jump to the same direction, you get a fail.
You will shoot up to 6 times and you can win or loose after 4 times, if its get all goals or fails in a row.
Its easy to follow how many penaltys are done and scoring of user and goalkeeper.
If you write wrong characters by mistake, you get a highlighted message to redone and the wrong input doesn´t counts in number of penaltys.

## Design
Since Python is a back end language, I havn´t focus on UX experience as much as the front end projects.
For a more game friendly enviroment, I have used some colours and design font 
I have also put in commando to clear the terminal for an easier action.

## Flowchart

A flow chart is made in[ Miro](https://miro.com/app/board/uXjVKJ1IWnU=/?share_link_id=523505058022)
There is a quite complex logic:
You make an input that compares to a random choice of compute.
If user win, it will return a "goal" result and if user fail, it will return another message.
You kick 6 times, but if you get the same result 4 times, you get over equal  and has already won.
Is the same otherwise.
If you have won, you end the game. Otherwise you continue to the end of 6 shoots.
You also need other algorithms, if you choose a non valid input, want to erad instructions and if you want to restart the game.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/04ea0225-34e7-45ce-bb96-b5ad42c8f9ff)



### Bugs / errors
Here is some examples through my project

* I got error in deployment after the first day and after research, I found a comma in the json file,t hat block the deployment.
* I tried to install and use pitch from mplsoccger for design, but I didnt get it through in the terminal and then I decided I skip that design

  
## Testing

## Technologies

Technologies I have used for this project:
Python - write the codes which are the base of the project
Github - Save the project in a repository
Google Drive - Instructions saved in a google document
Google cloud - API from Google documents to Python for instructions
Heroku - Deploy it to a public webside
Pyfiglet - Use of designed fonts 
Colorama - coloring the text

https://mplsoccer.readthedocs.io - I was thinking of create a soccer pitch from mpl soccer, but I changed my mind.



## Deployment
For deploying python codes, I use Heroku  app.

At first you commit everything to GitHub

After that you log in to HEROKU and create a new app.
![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/6bca34d3-0789-4bea-876b-78ee2d19bd68)

You connect the app to your repository in GitHub with same name

I choose to make a manual deploy, so I can see that everything goes ok and have controll of my first projekt.
![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/ac27a44c-d540-41ba-abfc-74c7ab49a862)


After you have deployed in HEROKU, you can visit your publish webside from Heroku or Github.
![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/648ac9c0-8260-4c73-b441-d1d369c62e51)


How to Fork
Should you wish to fork this repo, here is a guide on how to do that:

Firstly, go to https://github.com/emmy-codes/cat-adventures-python

On the main repo page, click the Fork button near the top right corner'
On the create a fork page, check the Owner of the repo is set to the GitHub org you wish to use, and change the name of the repo if you wish. 2a: Add a description if you want to
Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default)
Create the fork
Screenshot from an old project as I cannot fork my Python project due to not having any organizations connected to my account, and presumably because this repo is already a fork of the CI template

How to Clone
For cloning the repo you will need:

The repo open
Your IDE of choice
On the repo page, click on the green "Code" button
On the dropdown from the Code button, click on your chosen key (pictured here is SSH)
Click the copy button (shown as two squares on top of one another)
Open your IDE of choice and open the Terminal, or in my case, open the Terminal on your computer (I run Linux on Windows so may be slightly different for Mac/Windows users)
Check that you're in the right folder (shown here by checking my current folder by using the input: ls
Change as needed to reach your desired folder.
Type (without quotation marks): "git clone" followed by your copied link from GitHub.
You can now access the repo in your IDE if cloned directly there, or by typing (without quotation marks) "code ." in your Terminal.




## Acknowledgements

For this project, I have used the acknowledgement I´ve got from MPL and "loce sandwiches project" 
I used some videos and website for tutoring of some block of codes.

*https://trinket.io/python/909d6c5804- inspiration penalty definition
*https://www.giraffeacademy.com/programming-languages/python - tutoring of formatting
*https://www.w3schools.com/python - tutoring of formatting
*https://econowmics.com/python-penalty-kicks-simulator/ - function for penaltykicks
*https://www.101computing.net/penalty-shootout/ - tutoring video
*https://dcallanit.blogspot.com/2015/10/python-penalty-shoot-out.html - inspiration of penalty shoot game
*https://www.asciiart.eu/ 
*https://mplsoccer.readthedocs.io/en/latest/gallery/pitch_setup/plot_pitches.html - soccer pitch
*https://www.youtube.com/watch?app=desktop&v=u51Zjlnui4Y - tutoring colurs in Python
*https://docs.python.org/3/tutorial/errors.html - syntax error
*https://www.youtube.com/watch?v=Ovwr_Wt-og0 - tutoring pyfiglet

## Credits

* My mentor Gareth - gives me ideas and tips along the way.
* My schoolmate Josefine Yoshida Dahlqvist - always helpful and on my side :-) 

