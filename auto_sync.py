#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests


# In[157]:


import os


# In[162]:





# In[151]:


from jenkins import Jenkins
import xml.etree.ElementTree as ET


class jenkins_server:
    
    server = None
    username = None
    password = None
    
    server_point = None
    
    
    # template formatting details
    '''
    {0} = Git url
    
    {1} = script-path
    
    {2} = description
    
    '''
    
    job_template = """
<?xml version='1.0' encoding='utf8'?>
<flow-definition plugin="workflow-job@2.39">
  <actions>
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobAction plugin="pipeline-model-definition@1.7.1" />
    <org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction plugin="pipeline-model-definition@1.7.1">
      <jobProperties />
      <triggers />
      <parameters />
      <options />
    </org.jenkinsci.plugins.pipeline.modeldefinition.actions.DeclarativeJobPropertyTrackerAction>
  </actions>
  <description>{2}</description>
  <keepDependencies>false</keepDependencies>
  <properties />
  <definition class="org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition" plugin="workflow-cps@2.82">
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.3.0">
      <configVersion>2</configVersion>
      <userRemoteConfigs>
        <hudson.plugins.git.UserRemoteConfig>
          <url>{0}</url>
        </hudson.plugins.git.UserRemoteConfig>
      </userRemoteConfigs>
      <branches>
        <hudson.plugins.git.BranchSpec>
          <name>*/master</name>
        </hudson.plugins.git.BranchSpec>
      </branches>
      <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
      <submoduleCfg class="list" />
      <extensions />
    </scm>
    <scriptPath>{1}/jenkinsfile</scriptPath>
    <lightweight>true</lightweight>
  </definition>
  <triggers />
  <disabled>false</disabled>
</flow-definition>    
    """
    
    def __init__(self,server,username,password,port=8090):
        
        self.server_point = jenkins.Jenkins("http://"+server+":"+str(port)+"/", username=username, password=str(password))
        
        
    def lcom(command,split=True):
        if split:
            return os.popen(command).read().split("\n")
        else:
            return os.popen(command).read().split("\n")

    def sync():
        
        os.chdir("./Graph_Traversal")
        old_list = lcom("ggraph")
        os.system("git pull")
        
        
        new_list = lcom("ggraph")
        
        additions = [each for each in new_list if not in old_list]
        
        deletions = [each for each in old_list if not in new_list]
        
        
        if len(additions) == 0:
            print("no changes in system")
            
            return []
        
        else:
            
            for each in additions:
                
                temp = []
                
                if len(lcom("ggraph -p "+str(each))) !=0:
                    temp.append(each)
                    
            return temp
        
        
    def create_jenknisfile():
        
        return 0
    
    
    def create_pipe(self,name,script_path,url="https://github.com/YugantM/jenkins_repo.git"):
        
        conf = "".join(self.job_template.split("\n")).format(url,name,"This is a jenkins pipeline description")
        self.server_point.create_job(name,conf)
        
        return True


if __name__ == '__main__':
    
    server = jenkins_server("localhost",'yugantm','1234')
    
    if len(sync)>0:
        
        for each in sync():
            obj.create_pipe("pipe_"+each,each)
            
    else:
        
        print("No updates found")




