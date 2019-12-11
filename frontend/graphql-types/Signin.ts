/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: Signin
// ====================================================

export interface Signin_signin_user {
  __typename: "UserType";
  id: string;
  email: string;
  /**
   * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
   */
  username: string;
}

export interface Signin_signin {
  __typename: "SigninUser";
  user: Signin_signin_user | null;
}

export interface Signin {
  signin: Signin_signin | null;
}

export interface SigninVariables {
  email: string;
  password: string;
}
