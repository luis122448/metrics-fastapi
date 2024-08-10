pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'metrics-fastapi-app'
        PORT = credentials('metrics-fastapi')
        HOST_DATABASE_DIR = = credentials('metrics-fastapi')
    }

    stages {

        stage('Create .env file') {
            steps {
                writeFile file: '.env', text: """\
PORT=${env.PORT}
HOST_DATABASE_DIR=${env.HOST_DATABASE_DIR}
"""
                sh 'cat .env'
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'git@github.com:luis122448/metrics-fastapi.git'
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d'
                sh 'docker compose ps'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}
