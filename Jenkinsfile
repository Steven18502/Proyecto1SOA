pipeline {
    agent any
    stages {
        stage("init") {
            steps {
                git branch: 'test', changelog: true, poll: true, url: 'https://github.com/Steven18502/Proyecto1SOA.git'
            }
        }
        stage("build") {
            steps {
                dir('./cloud_function'){
                    sh 'pylint --exit-zero main.py'
                } 
            }
        }
        stage("test") {
            steps {
                dir('./cloud_function'){
                    echo 'pytest -v'
                } 
               
            }
        }
        stage("deploy") {
            steps {
                dir('./terraform'){
                    sh 'terraform init'
                    sh 'terraform plan'
                    //sh 'terraform destroy -auto-approve'
                } 
            }
        }
    }   
}
