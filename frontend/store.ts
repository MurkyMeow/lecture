import { State } from 'marycat'
import { Me_me } from './graphql-types/Me'

export const store = {
  user: new State<Me_me | null>(null),
}
