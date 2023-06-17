# AdoptMe

#### Video Demo:  <URL HERE>
  
### Description:
  Animal shelters are a rare sight in most places, this make the adoption process of rescue animals challenging. The unpredictability
  of these rescues and the willingness and the ability of the rescuers to adopt these animals gives them a lower chance to find a home.
  On the other hand, there are people who have the resources and the willingness to adopt a rescue animal but just can't find one. The
  main goal of this website is to connect these people and make the adoption process as easy as possible.
  
  ## Technical details:
  This is a database driven web application built on the Django Framework, it achieves some level of asynchronous functionality with
  websockets built using Django Channels and Redis.
  
  ## Apps:
  Inside the src/Adopt_Me (Root) directory the following apps will be found:
  
  ### Adopt_Me:
  This is the master directory that handles all of the apps' URLs and views for the HTTP/HTTPS requests and Routing and consumers for
  the websocket connections. The `settings.py` file is present in this directory.
  
  ### chats:
  This takes care of direct messages between any two users using websocket connections and channel layers.
  
  ### Data:
  This directory has the view that handles the search page. It queries the SQLite database for uploaded images of rescue animals by       rescuers.
  
  ### Members:
  Handles user login and registration using Django's inbuilt authentication system. The `forms.py` file has a registration from class
  inherits from `UserCreationForm` and styles the page with Bootstrap. 
  
  ### MyPosts:
  This is responsible for displaying the posts created by the logged in user. It uses a model imported from `upload` called `upload_img`
  The view also enables a user to edit their posts, if there are any.
  
  
  ### Product:
  Apologies for the irrelevant nomenclature, was my first Django app created as I was following a tutorial in the initial stages of this
  project. This is responsible for routing the homepage and the about page.
  
  
  ### static:
  contains a css file that includes the a font from google fonts for the entire page.
  
  
  ### Templates:
  Contains all the HTML templates arranged in directories corresponding to the above mentioned apps.
  
  
  ### Upload:
  This handles uploading of photos and other details that a rescuer might want to share about the animal. Contains the necessary
  models and model forms.
  
  
  ## Installation:
  It is recommended to use a virtual environment as this project has a lot of dependencies. Once added to your local machine, follow
  these steps:
  
  1. Install redis from `https://redis.io/docs/getting-started/installation/`.
  2. Run the command `pip install redis`.
     
  Note that the redis server must be running for live chat to function properly.

  








  
