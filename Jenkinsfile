def img
pipeline{
    environment{
        registry = "mhmmdtskr/hava_durumu_api"
        registryCredential = credentials("docker-hub-login")
        dockerImage = ""
        
    }
        agent any
        
        stages{
            stage("build checkout"){
                steps {
                    echo "checkout adımındayım"
                    git 'https://github.com/mhmmdtskr/HAVA_DURUMU_API.git'
                   
                }
            }
            
            stage ("build image"){
                steps {
                    echo "build image adımındayım"
                    script {
                        img = registry + ":v1"
                        println ("${img}")
                        dockerImage = docker.build ("${img}")
                    }
                }
            }
            
            stage ("Testing"){
                
                steps {
                    echo "test adımındayım"
                    sh "docker run -d --name ${JOB_NAME} -p 80:5000 ${img}"
                }
                
            }
            
            stage ("push to docker hub"){
                steps{
                    echo "push adımındayım"
                    script{
                        docker.withRegistry("https://registry.hub.docker.com", registryCredential){
                            dockerImage.push()
                        }
                    }
                }
                
            }
            
            
        }
}