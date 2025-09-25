def imageName = 'sakkoumhamza/book-loader'
def registry = 'https://index.docker.io/v1/'

node('workers') {
    stage('Checkout') {
        checkout scm
    }

    stage('Unit Tests') {
        sh "docker build -t ${imageName}-test -f Dockerfile.test ."
        sh 'docker run --rm -v "$(pwd)/reports:/app/reports" ' + imageName + '-test'
        junit "/Users/mac/.jenkins/workspace/books-loader_develop/reports/*.xml"
    }

    stage('Build') {
        sh "docker build -t ${imageName}:${commitID()} ."
    }

    stage('Push') {
         withCredentials([usernamePassword(credentialsId: 'registry', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
            sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"

            // Push with commit ID
            sh "docker push ${imageName}:${commitID()}"

            // Push 'develop' tag if on develop branch
            if (env.BRANCH_NAME == 'develop') {
                sh "docker push ${imageName}:develop"
            }

            sh "docker logout"
        }
    }
}

def commitID() {
    sh 'git rev-parse HEAD > .git/commitID'
    def commitID = readFile('.git/commitID').trim()
    sh 'rm .git/commitID'
    return commitID
}
