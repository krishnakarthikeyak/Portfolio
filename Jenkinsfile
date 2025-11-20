pipeline {
    agent any

    stages {

        stage('Pull Latest Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/krishnakarthikeyak/Portfolio.git'
            }
        }

        stage('Stop Old Containers') {
            steps {
                sh 'docker-compose down || true'
            }
        }

        stage('Build New Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Start Updated Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Cleanup Docker Garbage') {
            steps {
                sh 'docker system prune -af || true'
            }
        }

    }
}
