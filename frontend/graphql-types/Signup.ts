/* tslint:disable */
/* eslint-disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: Signup
// ====================================================

export interface Signup_signup_user {
  __typename: "UserType";
  id: string;
  email: string;
  /**
   * Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
   */
  username: string;
}

export interface Signup_signup_conflict {
  __typename: "SignupConflict";
  name: boolean | null;
  email: boolean | null;
}

export interface Signup_signup {
  __typename: "SignupUser";
  user: Signup_signup_user | null;
  conflict: Signup_signup_conflict | null;
}

export interface Signup {
  signup: Signup_signup | null;
}

export interface SignupVariables {
  email: string;
  name: string;
  password: string;
}
