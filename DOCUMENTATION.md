### Hello New Student. This is a step by step guide to a proper workflow.

#### Github Setup
Github is our version control and collaberation software, and I would be surprised if you have got this far without hearing of it.
Github allows one to always have a safe backup of code, to easily revert bad changes, to figure out who made bad changes, to test code on branches before merging it in, and so much more.

1. Make a github account, or login to one that already exists.
1. Make a new repository 
![Make a new Repository](/images/new_repository.PNG)
1. Use these settings for your new repository
![Use these settings for your new repository](/images/new_repository_settings.PNG)
1. Follow these instructions to initialize your new repository
	1. Instead of README.md, your first two initialized files should be DOCUMENTATION.md and CHANGELOG.md
![Follow these instructions to initialize your new repository](/images/new_repository_instructions.PNG)

#### Docker Setup
Docker is our Unit-Testing and Enviornment software. Because programs often run differently on different OS's; it helps to have an enviornment which you control completely. Docker allows this by creating a virtual machine.
Docker can also be configured to automatically test new code as you upload it to github.

1. Make a docker cloud account, or login to one that already exists
1. Create a new repository, and connect it to your github repository
![a](/images/docker_connect.PNG)
1. Configure automated pull requests.
	1. Go to builds, and click Conifigure Automated Builds
	1. Set it up like this
![a](/images/docker_autobuild.PNG)

#### Create a pull request
We always want to keep our master branch on github in a workable state. To that end we use pull request when adding new code so it doesn't break the master branch. Whenever a new feature is created, a new pull request should be created with it.
This works because of the way branches work in github. Its like the branches of a tree.

1. Open your command line, and go to your repository.
1. Enter the following command "git checkout -b builddocker"
1. Add all the files to git "git add *"
1. create a commit "git commit -m "your message""
1. Enter the following command "git push origin builddocker"
1. Create a pull request
![a](/images/Pull_Request)

#### Set up the Docker Virtual Machine and Unit Tests
We may have set up the docker cloud, but we need to give docker its instructions to build an enviorment.
We should also set some tests up so we know whether our program works.
We want to set the tests up first because we want to know if the tests work before we do the actual code.

1. Make certain you are on your new branch.
1. Create the dockerfile, which sets up the virtual machine enviornment. Its contents are as follows.
![](/images/Dockerfile.PNG)
1. Create docker-compose.test.yml. Contents are as follows.
![](/images/Compose.PNG)
1. Create run_test.sh. Contents are as follows
![](/images/Run_Tests.PNG)
1. Create the python file which actually contains the unit tests. Contents are as follows
![](/images/test.PNG)
1. Push changes up to github using instructions from pull requests.



