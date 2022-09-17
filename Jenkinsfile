pipeline {
    agent any
    stages {
        stage("git") {
            steps {
                git branch: 'main', changelog: true, poll: true, url: 'https://github.com/Steven18502/Proyecto1SOA.git'
            }
        }
        stage("CodeCheck") {
            steps {
                dir('./cloud_function'){
                    sh 'pylint --exit-zero main.py'
                    sh 'pylint --exit-zero database.py'
                } 
            }
        }
        stage("test") {
            steps {
                dir('./cloud_function'){
                    sh 'pytest -v'
                } 
               
            }
        }
        stage("deploy") {
            steps {
                dir('./terraform'){
                    sh 'terraform init'
                    sh 'terraform plan'
                    sh 'terraform apply -auto-approve'
                } 
            }
        }
    }   
}
