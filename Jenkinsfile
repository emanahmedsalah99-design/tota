
pipeline {
    agent any

    environment {
        APP_NAME      = 'web-app'
        REPO_URL      = 'https://github.com/emanahmedsalah99-design/tota.git'
        DOCKER_IMAGE  = 'emma175/web-app'
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                git branch: "${GIT_BRANCH}",
                    credentialsId: 'github',
                    url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${APP_NAME}:${BUILD_NUMBER} .
                """
            }
        }

        stage('Tag Docker Image') {
            steps {
                sh """
                    docker tag ${APP_NAME}:${BUILD_NUMBER} ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker tag ${APP_NAME}:${BUILD_NUMBER} ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Docker Hub Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh """
                        docker login -u $DOCKER_USER -p $DOCKER_PASS
                    """
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh """
                    docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                    docker run -d -p 5000:5000 \
                    --name ${APP_NAME}-${GIT_BRANCH}-${BUILD_NUMBER} \
                    ${DOCKER_IMAGE}:${BUILD_NUMBER}

                    docker ps
                """
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline SUCCESS: Image pushed and container running successfully."
        }

        failure {
            echo "❌ Pipeline FAILED: Check Jenkins logs for details."
        }

        always {
            echo "📌 Pipeline finished at: ${new Date()}"
        }
    }
}
