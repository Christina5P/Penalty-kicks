# Penalty Kicks

Live link:
https://penaltykicks-dd69cb0985ef.herokuapp.com/

Penalty kicks are a back-end game, based on algorithms.
You don´t need to be a brilliant soccer player to have a chance in this game, just luck! 
You start up the game by writing your name and taking a chance to name yourself as a famous soccer player and get the illusion of winning with penalty shots.
You will be asked to read instructions or not, so you don´t always have to scroll down a lot of text if you don't need to.
You don´t have to be nervous about making a mistake or breaking something, since you get an error message and a retry if you don't use a valid input. 
When the game ends you get questioned if you want to restart or not.
My idea for this game comes out of the soccer players in my family who wish to practice the algorithm that comes with Python.
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
When the game starts you have 6 directions to choose for the penalty: Left top or bottom, Middle top or bottom, or Right Top or bottom.
They are shortened code, so it´s easy to text, but are explained so you don't get confused or have to remember the codes.
After your choice, the computer makes a random choice of which direction the goalkeeper will jump. If he jumps in the same direction, you get a fail.
You will shoot up to 6 times and you can win or lose after 4 times if it gets all goals or fails in a row.
It's easy to follow how many penalties are done and the scoring of the user and goalkeeper.
If you write wrong characters by mistake, you get a highlighted message to redone and the wrong input doesn´t count in several penalties.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/b6100b42-cf35-4c4a-bf0d-8b3f81f2e7f4)

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/3ab86b4d-b434-4191-bd94-72199e14e324)


![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/20a396c5-865e-4d75-9b0e-48425dcf93f0)


## Design
Since Python is a back-end language, I haven´t focused on UX experience as much as the front-end projects.
For a more game-friendly environment, I have used some colors and design font.
I have also put in commando to clear the terminal for easier action.

Through the project, I investigated some design potions from mpl soccer, and turtle and also drew a soccer cage with Python codes, but decided to drop those functions.


## Flowchart

A flow chart is made in[ Miro](https://miro.com/app/board/uXjVKJ1IWnU=/?share_link_id=523505058022)
There is a quite complex logic: You make an input that compares to a random choice of compute.
If the user wins, it will return a "goal" result and if the user fails, it will return another message.
You kick 6 times, but if you get the same result 4 times, you get over equal and have already won. Is the same otherwise.
If you have won, you end the game. Otherwise, you continue to the end of 6 shoots.
You also need other algorithms, if you choose a nonvalid input, want to read instructions, and if you want to restart the game.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/04ea0225-34e7-45ce-bb96-b5ad42c8f9ff)



### Bugs / errors
Here are some examples from my project
* I got an error in deployment after the first day and after research, I found a comma in the JSON file, that blocked the deployment.

* I tried to install and use pitch from mplsoccer for design, but I didn't get it through in the terminal and then I decided I skip that design

* I tried to draw Circel with turtle(thought of a moving soccer ball) 
but it wasn't compatible with gitpod codespace

* I got styleproblem for information of numberof penaltys and scores (too much space
 between goalkeepers choices of direction). I tried to style it in different ways,
  as \t, \n and 
  f"{directions[goalkeeper_group[0]]:<20},{directions[goalkeeper_group[1]]:<5}",
  I hasn´t got a really god effect of the styling.

* You get goal 90% of time
  I fixed it by changing the rules of the goalkeeper's catch. 
  I made one more function with groups, so the goalkeeper covered up both up and down in each direction. 
  
## Testing

* valid https://pep8ci.herokuapp.com/
 ![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/03d487e3-64a7-4bb4-ac4e-983fa52c2f2f)
It is 1 note of 1 line too long in the validation.
I tried to shorten the line, but then I got errors that the API didn´t work, so I decided to keep the link on one line.

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

https://mplsoccer.readthedocs.io -  I was thinking of creating a soccer pitch from mpl soccer, but I changed my mind.


## Deployment
For deploying Python codes, I use the Heroku app.
At first, you commit everything to GitHub 
After that you log in to HEROKU and create a new app.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/6bca34d3-0789-4bea-876b-78ee2d19bd68)

You connect the app to your repository in GitHub with the same name 
I choose to make a manual deployment, so I can see that everything goes ok and have control of my first project.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/ac27a44c-d540-41ba-abfc-74c7ab49a862)

After you have deployed in HEROKU, you can visit your published website from Heroku or Github.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/648ac9c0-8260-4c73-b441-d1d369c62e51)


### How to Fork
You can fork this repo if you want to have your copy on your repository to work with.
To fork, you click the fork button at the top of the right corner of the main repo.
On the Create a Fork page, change the name of the repo if you wish. 
Check the box here if you want to make a copy of the main branch or multiple branches (main is selected by default) Create the fork.

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/b0e66870-8451-41bc-adce-889ce9f94d3a)


### How to Clone
if you clone the repo, you create a copy of the repo in your repo (with all files and history)
It creates a remote to the original repo, so you can work in your copy and push it back to the original.
Open your repo and go to the green button "code" on the right-hand side. The easiest way is to open it with GitHub desktop: 

![image](https://github.com/Christina5P/Penalty-kicks/assets/160019695/fdbd43b0-56d7-41f1-b05c-2a0b5508b109)

You can read more information on cloning at the GitHub : https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository



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
### https://www.educative.io/answers/what-is-randomsample-in-python -tutoring about random sample
### https://www.youtube.com/watch?v=Ovwr_Wt-og0 - tutoring pyfiglet
### https://www.youtube.com/watch?v=2h8e0tXHfk0 - typewriting style
### https://app.grammarly.com/ddoc -spellchecking
### https://monica.im/home - chat generator to solve the stylingproblem of scores

## Credits

* My mentor Gareth - gives me ideas and tips along the way.
* My schoolmate Josefine Yoshida Dahlqvist - always helpful and on my side :-) 
* My student fellows Niklas Hugdahl and Ahmed

