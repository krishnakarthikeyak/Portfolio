pipeline{
    agent any
    stages{
        stage('Clone repo'){
            steps{
                git branch: 'master', url: 'https://github.com/krishnakarthikeyak/Portfolio.git'
            }
        }
        stage('Build image'){
            steps{
                sh 'docker compose build '
            }
        }
        stage('Deploy with docker compose'){
            steps{
                // existing container if they are running
                sh 'docker compose down || true'
                // start app, rebuilding flask image
                sh 'docker compose up -d --build'
            }
        }
        stage('Cleanup Docker Garbage') {
            steps {
                sh 'docker system prune -af || true'
            }
        }
    }
}




