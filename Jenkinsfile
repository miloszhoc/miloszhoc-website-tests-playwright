pipeline {
  agent any

  stages {
    stage("Setup") {
      steps {
        sh 'ls'
      }
    }

    stage("Execution") {
      steps {
        sh 'python --version'
      }
    }
    stage("Report") {
      steps {
        sh 'echo "report"'
      }
    }

  }
}
