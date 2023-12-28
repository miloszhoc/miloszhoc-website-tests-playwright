pipeline {
  agent any

  stages {
    stage("Setup") {
      steps {
        sh 'pwd'
        sh 'ls'
        sh 'ls ..'

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
