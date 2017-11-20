# profileapp

In project re realised next steps:
1. Create django project.
Use some tool to deploy development environment (e.g. virtualenv)
Create profile app (first name, last name, data of birth, biography,
contacts).
Add front page, where you'll show your profile data (use fixtures).
2. Add authentication for this page.
3. Create middleware that stores all requests and execution time.
4. Create template context processor that add django.conf.settings to
context.
5. Create a page where you may change your profile.
6. forms-widgets - assign calendar widget to "date of birth" field.
7. forms-model-extra - (edit profile form has been done with
forms.ModelForm? ;)
8. template-tags - create template tag, that gets any model object
9. commands - create django command that prints all models and object
counts.
10. signals - create signal handler, that creates a note in database when
every model is created/edited/deleted.(used django-simple-history)
Bonuses:
* Use some tools to easily deploy dev environment (at least requirements.txt file, next level - vagrant or docker)
* Use some front-end grid library (e.g. Bootstrap)
