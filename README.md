# Assignment 4 
[![Docker Pulls](https://badgen.net/docker/pulls/warlicks/flask-app-2?icon=docker&label=pulls)](https://hub.docker.com/r/warlicks/flask-app-2/)


In this assignment we expanded on building application that we have been developing in 
class. 

I updated the main page so that the three accordions display locations for a particular type of business on a carousel; restaurants, hotels and attractions. I modified the carousels to remove the indicators that are present by default. This change required updating the [index template](templates/index.html) and [app.py](app.py)

I also modified the page to remove the type of categories from the navigation bar. It was replaced with an About page. To create the About page in created [templates/about.html](templates/about.html). I then added a new route `\about` in [app.py](app.py). This renders the template. 

The third major change that I made was adding a background image to the site. I did this by modifying the [templates/base.html](templates/base.html). There I updated the `<style>` tag and added a `background-image:`. 

The final change that I made is small change in [templates/base.html](templates/base.html). There I modified the footer. 

Once the modifications were build I created a new docker container and published it to [Docker Hub](https://hub.docker.com/r/warlicks/flask-app-2/). From there I deployed the application on an EC2 instances. 
