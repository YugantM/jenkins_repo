# jenkins_repo


This repository contains multiple jenkinsfile in subdirectories.



Installing jenkins in arch-linux:

```shell
sudo pacman -S jenkins
```

Start the server by following command:

```shell
sudo systemctl start jenkins
```

Check the status of jenkins server:

```shell
sudo systemctl status jenkins
```

Find the admin password using following command:

```shell
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Create user, follow the web ui steps. [link](sudo cat /var/lib/jenkins/secrets/initialAdminPassword)

The default port of jenkins is **8090**. To open locally browse: localhost:8090

From virtual machine typy in <IP_Address>:8090



Below is the landing page of the Jenkins

<img src="./Screenshot 2020-09-01 at 2.34.06 PM.png">


Select pipeline and enter the name:

<img src="./Screenshot 2020-09-01 at 2.38.49 PM.png">


### Writing groovy script



#### 1 JenkinsFile in the repo

Go to Advanced Project Options >> Definition, select Pipeline script from SCM:
<img src="./Screenshot 2020-09-01 at 2.50.38 PM.png">


Select Git as SCM and paste the link of the github repository:
<img src="./Screenshot 2020-09-01 at 2.55.03 PM.png">


Next, add the subdirectory path if required. Jenkins looks for the jenkinsfile in the root directory of the repo if path is provided explicitly
<img src="./Screenshot 2020-09-01 at 2.57.22 PM.png">


#### 2 Select definition as Pipeline script and adit it write away
<img src="./Screenshot 2020-09-01 at 3.01.24 PM.png">


## Writing JenkinsFile

 **Basic structure**

<img src="./untitled (6).png">


Sample script:

```groovy
pipeline{
  
    agent any
    stages {
        stage('Cloning') {
            steps {
                echo 'Cloning..'
              	git url: 'URL'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
  
}
```





# auto_sync.py

This script can create jobs by checking the current state of the system and old state.



**Following steps are executed in order to create the Jenkins jobs:**

1. Connecting to Jenkins Server. (method of user configuration of linux tool is not known yet)
2. Creates dependency graph of the the packages (folder with the PKGBUILDs in sub-folders)
3. Pulls the git repo
4. Creates dependency graph of the the packages (folder with the PKGBUILDs in sub-folders)
5. Comapre two dependecy graphs and creates a new graph which indicates the changes.
6. All the changes are detected like new package added, relation among the packages change or deletion.
7. The list is created for the changed modules and a dependency sub-graph is generated for them.
8. The main function follows the ordered-list of packages and creates a job if the job is not  already present in the Jenkins server.



### Notes

* *Triggering part is yet to be added*.
* *Common json structure is yet to be implemented.*
* *Automatic creation of jenkinsfiles not added.*

