# Penalty Kicks

Live link:
https://penaltykicks-dd69cb0985ef.herokuapp.com/

Penalty kicks is a back end game, based on algorithms.
You don´t need to be a brilliant soccerplayer to have a chance in this game, just luck!
You start up the game with writing your name, and take a chance to name yourself as a famous soccerplayer and get the illusion to win with penalty shoots.
You will be asked to read instructions or not, so you don´t always have to schroll down a lot of text if you dont need to.
You don´t have to be nervous to make a misstake or break someting, since you get an errormessage and a retry if you dont use a valid input.
When the game ends you get questioned if you want to restart or not.

My idea for this game comes out of my soccerplayers in family and wish to practice the algorithm that comes with python.
When you are going to shoot that penalty "on life or death" you have to make a strategy and lot of thinking.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/fdffaf65-bcad-44c3-afe2-c9763a33fb44)


## Contents

*  [Features](#features)
*  [Design](#design)
*  [Flowcharts](#flowcharts)
*  [Bugs / errors](#Bugs/errors)
*  [Test](#test)
*  [Technologies](#Technologies)
*  [Deployment](#Deployment)
*  [Acknowledgement](#Acknowledgement)
*  [Credits](#Credits)
  

## Features
When the game starts you have 6 directions to choose for the penalty: Left top or bottom, Middle top or bottom or Right Top or bottom.
They are shortened code, so it´s easy to text, but are explained so you dont get confused or have to remember the codes.
After your choice the computer makes a random choice which direction the goalkeeper will jump. If he jump to the same direction, you get a fail.
You will shoot up to 6 times and you can win or loose after 4 times, if its get all goals or fails in a row.
Its easy to follow how many penaltys are done and scoring of user and goalkeeper.
If you write wrong characters by mistake, you get a highlighted message to redone and the wrong input doesn´t counts in number of penaltys.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/b6100b42-cf35-4c4a-bf0d-8b3f81f2e7f4)

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/3ab86b4d-b434-4191-bd94-72199e14e324)


![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/20a396c5-865e-4d75-9b0e-48425dcf93f0)


## Design
Since Python is a back end language, I havn´t focus on UX experience as much as the front end projects.
For a more game friendly enviroment, I have used some colours and design font.
I have also put in commando to clear the terminal for an easier action.

Through the project I have investigate some design potions from mpl soccer, turtle and also drawing a soccercage with python codes, but decided to drop those functions.

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
* I tried draw circel (thought of a moving soccervall) but it wasnt compatible with gitpod codespace

  
## Testing

* valid https://pep8ci.herokuapp.com/
 ![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/03d487e3-64a7-4bb4-ac4e-983fa52c2f2f)
It is 1 notes of 1 line too long in the validation.
I tried to shorten the line, but then I got errors that API didn´t worked, so I decided to keep the link on one line.

I have done manual testing of every moment in the game, so everything works.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/3643c6f5-c8d4-46d8-a60e-ca972af69c72)


## Technologies

Technologies I have used for this project:
* Python -Language of this project
* Github - Save the project in a repository
* Google Drive - Instructions saved in a google document
* Google cloud - API from Google documents to Python for instructions
* Heroku - Deploy it to a public webside
* Pyfiglet - Use of designed fonts 
* Colorama - coloring the text

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


### How to Fork
You can fork this repo if you want to have an own copy on your own repository to work with.

To fork, you click the fork button on top of right corner in main repo.
On the create a fork page, change the name of the repo if you wish.
Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default)
Create the fork.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/b0e66870-8451-41bc-adce-889ce9f94d3a)


### How to Clone
If you clone the repo, you create a copy of the repo in your own repo (with all files and history)
It creates a remote to the original repo, so you can work in your copy and push it back to original.

Open your repo and go to the green button "code" on right hand side.
Easiest way is to open with github desktop:
![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/fdbd43b0-56d7-41f1-b05c-2a0b5508b109)

You can read more information of cloning at Github page: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository



## Acknowledgements

For this project, I have used the acknowledgement I´ve got from MPL and "loce sandwiches project" 
I used some videos and website for tutoring of some block of codes.

### https://trinket.io/python/909d6c5804- inspiration penalty definition
### https://www.giraffeacademy.com/programming-languages/python - tutoring of formatting
### https://www.w3schools.com/python - tutoring of formatting
### https://econowmics.com/python-penalty-kicks-simulator/ - function for penaltykicks
### https://www.101computing.net/penalty-shootout/ - tutoring video
### https://dcallanit.blogspot.com/2015/10/python-penalty-shoot-out.html - inspiration of penalty shoot game
### https://mplsoccer.readthedocs.io/en/latest/gallery/pitch_setup/plot_pitches.html - soccer pitch
### https://www.youtube.com/watch?app=desktop&v=u51Zjlnui4Y - tutoring colurs in Python
### https://docs.python.org/3/tutorial/errors.html - syntax error
### https://www.youtube.com/watch?v=Ovwr_Wt-og0 - tutoring pyfiglet

## Credits

* My mentor Gareth - gives me ideas and tips along the way.
* My schoolmate Josefine Yoshida Dahlqvist - always helpful and on my side :-) 

