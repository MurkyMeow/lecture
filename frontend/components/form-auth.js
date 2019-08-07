import { webc, _if, State } from 'marycat'
import { Button } from './button'
import { Toggle } from './toggle'
import notification from '../notification'
import css from './form-auth.css'
import * as api from '../api'

export const FormAuth = webc({
  name: 'lecture-form-auth',
  css,
  props: {
    signup: true,
  },
  render(h) {
    const data = new State()
    const option = new State()
    const submit = async () => {
      const url = `/auth/${signup.v ? 'signup' : 'signin'}/`
      try {
        await api.post(url, data)
      } catch (err) {
        notification.show(err, 'error')
      }
    }
    return h
    (form().submit(submit)
      (Toggle().between(['🔑', '👽']).bind(option))
      (input('@email').type('email')
        .placeholder('Email')
        .required()
      )
      (input('@password').type('password')
        .placeholder('Пароль')
        .required()
      )
      (_if(option.eq('👽'))
        (input('@password_again').type('password')
          .placeholder('Повторите пароль')
          .required()
        )
        (input('@name')
          .placeholder('Никнейм')
          .required()
        )
      )
      (Button().text('Продолжить'))
    )
  },
})
