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
  
  ## Django Apps:
  Inside the src/Adopt_Me (Root) directory the following apps will be found:
  
  ### Adopt_Me:
  This is the master directory that handles all of the apps' URLs and views for the HTTP/HTTPS requests and Routing and consumers for
  the websocket connections. The `settings.py` file is present in this directory.
