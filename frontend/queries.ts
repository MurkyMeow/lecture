import gql from 'graphql-tag'

export const GET_ME = gql`
  query Me {
    me {
      id
      email
      username
    }
  }
`
export const SIGNOUT = gql`
  mutation Signout {
    signout {
      ok
    }
  }
`
export const SIGNUP = gql`
  mutation Signup($email: String!, $name: String!, $password: String!) {
    signup(email: $email, name: $name, password: $password) {
      user {
        id
        email
        username
      }
      conflict {
        name
        email
      }
    }
  }
`
export const SIGNIN = gql`
  mutation Signin($email: String!, $password: String!) {
    signin(email: $email, password: $password) {
      user {
        id
        email
        username
      }
    }
  }
`
