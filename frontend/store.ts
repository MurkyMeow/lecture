import { State } from 'marycat'

export type User = { username: string }

export const store = {
  user: new State<User | null>(null),
}
