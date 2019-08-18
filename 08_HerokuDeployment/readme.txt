# Heroku Deployment

1. Create your flask app.
2. Install gunicorn - > pip install gunicorn
3. Create requirement.txt -> pip freeze > requirements.txt
4. Create process file "Procfile" -> echo "web: gunicorn app:app" > Procfile (CASE SENSITIVE)
5. Download and Install Heroku CLI
6. Create Heroku account
7. Create New App --> Set app name "flask-app-test-deploy"
8. Heroku CLI login: Open command prompt and type -> heroku login
9. CD to base dir and initialize GIT -> git init
(newFlaskEnv) D:\Udemy\Flask-Bootcamp-master\flask-bootcamp\08_HerokuDeployment>git init
Initialized empty Git repository in D:/Udemy/Flask-Bootcamp-master/flask-bootcamp/08_HerokuDeployment/.git/

10. initialize remote -> heroku git:remote -a flask-app-test-deploy
(newFlaskEnv) D:\Udemy\Flask-Bootcamp-master\flask-bootcamp\08_HerokuDeployment>heroku git:remote -a flask-app-test-deploy
 »   Warning: heroku update available from 7.22.2 to 7.27.1
set git remote heroku to https://git.heroku.com/flask-app-test-deploy.git

11. Git add -> git add .
12. Git commit -> git commit -am "initial commit"
13. Git push - > git push heroku master
